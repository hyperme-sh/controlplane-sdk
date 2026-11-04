"""Validate emitted REST operations and keep legacy usage-client imports usable."""

from __future__ import annotations

import ast
import re
from pathlib import Path

METHODS = frozenset(
    {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
)
TAG_NAMES = {"ai": "AIUsage"}


def map_codegen_tags(document):
    for item in document.get("paths", {}).values():
        for method, operation in item.items():
            if method.lower() in METHODS:
                operation["tags"] = list(
                    dict.fromkeys(
                        TAG_NAMES.get(tag, tag)
                        for tag in operation.get("tags", ["default"])
                    )
                )
    for tag in document.get("tags", []):
        tag["name"] = TAG_NAMES.get(tag["name"], tag["name"])
    groups = {}
    for item in document.get("paths", {}).values():
        for method, operation in item.items():
            if method.lower() in METHODS:
                for tag in operation["tags"]:
                    previous = groups.setdefault(tag.casefold(), tag)
                    if previous != tag:
                        raise ValueError(
                            f"Case-colliding SDK tags require an explicit mapping: {previous}, {tag}"
                        )
    return document


def expected_operations(document):
    return {
        (method.upper(), path)
        for path, item in document["paths"].items()
        for method in item
        if method.lower() in METHODS
    }


def emitted_operations(root: Path, language: str):
    result = set()
    manifest = root / ".openapi-generator/FILES"
    managed = set(manifest.read_text().splitlines()) if manifest.exists() else None

    def sources(directory, pattern):
        return (
            path
            for path in directory.glob(pattern)
            if managed is None or path.relative_to(root).as_posix() in managed
        )

    if language == "python":
        paths = sources(root / "openapi_client/api", "*.py")
        for path in paths:
            for node in ast.walk(ast.parse(path.read_text())):
                if isinstance(node, ast.Call):
                    values = {
                        kw.arg: kw.value.value
                        for kw in node.keywords
                        if isinstance(kw.value, ast.Constant)
                    }
                    if "method" in values and "resource_path" in values:
                        result.add((values["method"], values["resource_path"]))
    elif language == "typescript-fetch":
        for path in sources(root / "apis", "*.ts"):
            for match in re.finditer(
                r"path:\s*`([^`]+)`[^\n]*,\s*method:\s*['\"]([A-Z]+)['\"]",
                path.read_text(),
            ):
                result.add((match[2], match[1]))
    elif language == "kotlin":
        for path in sources(
            root / "src/main/kotlin/org/openapitools/client/apis", "*.kt"
        ):
            result.update(
                (match[1], "/" + match[2].lstrip("/"))
                for match in re.finditer(
                    r'@(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|TRACE)\("([^\"]+)"',
                    path.read_text(),
                )
            )
    elif language == "swift5":
        for path in sources(root / "OpenAPIClient/Classes/OpenAPIs/APIs", "*.swift"):
            for match in re.finditer(
                r'(?:let|var) localVariablePath = "([^\"]+)"[\s\S]*?\.init\(method: "([A-Z]+)"',
                path.read_text(),
            ):
                result.add((match[2], match[1]))
    else:
        raise ValueError(f"Unsupported REST client language: {language}")
    return result


def validate_generated_operations(root: Path, language: str, document):
    expected = expected_operations(document)
    actual = emitted_operations(root, language)
    if actual != expected:
        raise ValueError(
            f"{language} operation coverage mismatch: missing={sorted(expected - actual)}, extra={sorted(actual - expected)}"
        )
    # Never rely on case-sensitive CI to accept a tree unusable on consumer disks.
    api_paths = {
        "python": "openapi_client/api",
        "typescript-fetch": "apis",
        "kotlin": "src/main/kotlin/org/openapitools/client/apis",
        "swift5": "OpenAPIClient/Classes/OpenAPIs/APIs",
    }
    names = {}
    for path in (root / api_paths[language]).iterdir():
        previous = names.setdefault(path.name.casefold(), path.name)
        if previous != path.name:
            raise ValueError(
                f"Case-colliding SDK API filenames: {previous}, {path.name}"
            )


def install_usage_compatibility(root: Path, language: str):
    """Preserve previous usage entrypoints without case-colliding source files."""
    written = []
    usage_paths = {
        "python": "openapi_client/api/ai_usage_api.py",
        "typescript-fetch": "apis/AIUsageApi.ts",
        "kotlin": "src/main/kotlin/org/openapitools/client/apis/AIUsageApi.kt",
        "swift5": "OpenAPIClient/Classes/OpenAPIs/APIs/AIUsageAPI.swift",
    }
    if not (root / usage_paths[language]).is_file():
        return written
    # These new clients come from templates with trailing comment whitespace.
    # Normalize them as part of generation, rather than editing generated output.
    usage_files = [usage_paths[language]]
    usage_files += {
        "python": ["test/test_ai_usage_api.py"],
        "kotlin": ["src/test/kotlin/org/openapitools/client/apis/AIUsageApiTest.kt"],
    }.get(language, [])
    for name in usage_files:
        path = root / name
        if path.is_file():
            path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()).rstrip() + "\n")
    if language == "python":
        text = "\n# Legacy usage API name; the canonical implementation has its own module.\nfrom openapi_client.api.ai_usage_api import AIUsageApi as AiApi\n"
        legacy = "openapi_client/api/ai0_api.py"
        (root / legacy).write_text(text)
        written.append(legacy)
        for name in (
            "openapi_client/__init__.py",
            "openapi_client/api/__init__.py",
            "openapi_client/api/ai_api.py",
        ):
            path = root / name
            path.write_text(path.read_text() + text)
            written.append(name)
    elif language == "typescript-fetch":
        # APIs sharing tagged operations can also emit duplicate request types.
        # Retain the first barrel name and expose subsequent types with their API
        # prefix; each original name remains available in its own module.
        index = root / "apis/index.ts"
        seen = set()
        lines = []
        for line in index.read_text().splitlines():
            match = re.fullmatch(r"export \* from './([^']+)';", line)
            if match:
                module = match[1]
                exports = re.findall(
                    r"export (class|interface) (\w+)",
                    (root / "apis" / f"{module}.ts").read_text(),
                )
                if any(symbol in seen for _, symbol in exports):
                    for kind, symbol in exports:
                        alias = (
                            f"{symbol} as {module}{symbol}"
                            if symbol in seen
                            else symbol
                        )
                        type_only = "type " if kind == "interface" else ""
                        lines.append(
                            f"export {type_only}{{ {alias} }} from './{module}';"
                        )
                else:
                    lines.append(line)
                seen.update(symbol for _, symbol in exports)
            else:
                lines.append(line)
        index.write_text("\n".join(lines) + "\n")
        name = "apis/Ai0Api.ts"
        (root / name).write_text(
            "// Compatibility for the previous generated usage module.\n"
            "export * from './AIUsageApi';\n"
            "export { AIUsageApi as AiApi } from './AIUsageApi';\n"
            "export type { AIUsageApiInterface as AiApiInterface } from './AIUsageApi';\n"
        )
        path = root / "apis/index.ts"
        path.write_text(
            path.read_text() + "export { AIUsageApi as AiApi } from './AIUsageApi';\n"
            "export type { AIUsageApiInterface as AiApiInterface } from './AIUsageApi';\n"
        )
        written += [name, "apis/index.ts"]
    elif language == "kotlin":
        name = "src/main/kotlin/org/openapitools/client/apis/Ai0Api.kt"
        (root / name).write_text(
            "package org.openapitools.client.apis\n\n"
            "// Retain the previous JVM interface, including inherited Retrofit annotations.\n"
            "interface AiApi : AIUsageApi\n"
        )
        written.append(name)
    elif language == "swift5":
        name = "OpenAPIClient/Classes/OpenAPIs/APIs/Ai0API.swift"
        (root / name).write_text(
            "// Retain the previous usage-client name in the generated module.\n"
            "public typealias AiAPI = AIUsageAPI\n"
        )
        written.append(name)
    return written
