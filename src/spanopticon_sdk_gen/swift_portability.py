"""Keep the generated URLSession transport buildable with Linux Foundation."""
from pathlib import Path
import re


def install_swift_portability(root: Path) -> list[str]:
    name = 'OpenAPIClient/Classes/OpenAPIs/URLSessionImplementations.swift'
    path = root / name
    text = path.read_text()
    text = text.replace(
        'import Foundation\n#if !os(macOS)\nimport MobileCoreServices\n#endif',
        'import Foundation\n#if canImport(FoundationNetworking)\n'
        'import FoundationNetworking\n#endif\n'
        '#if canImport(MobileCoreServices)\nimport MobileCoreServices\n'
        '#elseif canImport(CoreServices)\nimport CoreServices\n#endif',
    )
    text = text.replace(
        '            if let uti = UTTypeCreatePreferredIdentifierForTag',
        '            #if canImport(MobileCoreServices) || canImport(CoreServices)\n'
        '            if let uti = UTTypeCreatePreferredIdentifierForTag',
    ).replace(
        '                return mimetype as String\n            }',
        '                return mimetype as String\n            }\n            #endif',
    )
    path.write_text(text)
    validation_name = 'OpenAPIClient/Classes/OpenAPIs/Validation.swift'
    validation = root / validation_name
    # Keep the server's ValidationError wire model name. The generated generic
    # validation helper otherwise redeclares it in the same Swift module.
    validation.write_text(re.sub(r'\bValidationError\b', 'SchemaValidationError',
                                 validation.read_text()))
    return [name, validation_name]
