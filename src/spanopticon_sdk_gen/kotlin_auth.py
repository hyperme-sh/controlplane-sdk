"""Remove identical declarations emitted once per bearer security scheme."""
from pathlib import Path
import re


def install_kotlin_auth(root: Path) -> list[str]:
    name = 'src/main/kotlin/org/openapitools/client/infrastructure/ApiClient.kt'
    path = root / name
    text = path.read_text()
    seen: set[str] = set()

    def once(match: re.Match[str]) -> str:
        declaration = match.group(0)
        if declaration in seen:
            return ''
        seen.add(declaration)
        return declaration

    text = re.sub(r'^import [^\n]+\n', once, text, flags=re.MULTILINE)
    # Only byte-identical declarations are removed; auth scheme names and the
    # constructor's dispatch table remain intact.
    text = re.sub(r'^    (?:constructor\(|fun setBearerToken\()[\s\S]*?^    }\n',
                  once, text, flags=re.MULTILINE)
    path.write_text(text)
    return [name]
