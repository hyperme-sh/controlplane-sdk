"""Keep the generated URLSession transport buildable with Linux Foundation."""
from pathlib import Path
import re


def _replace_known(text: str, old: str, new: str) -> str:
    if text.count(new) == 1 and old not in text:
        return text
    if text.count(old) != 1 or new in text:
        raise ValueError('Unexpected Swift generator template; review portability transform')
    return text.replace(old, new)


def install_swift_portability(root: Path) -> list[str]:
    name = 'OpenAPIClient/Classes/OpenAPIs/URLSessionImplementations.swift'
    path = root / name
    text = _replace_known(
        path.read_text(),
        'import Foundation\n#if !os(macOS)\nimport MobileCoreServices\n#endif',
        'import Foundation\n#if canImport(FoundationNetworking)\n'
        'import FoundationNetworking\n#endif\n'
        '#if canImport(MobileCoreServices)\nimport MobileCoreServices\n'
        '#elseif canImport(CoreServices)\nimport CoreServices\n#endif',
    )
    old = '''            if let uti = UTTypeCreatePreferredIdentifierForTag(kUTTagClassFilenameExtension, pathExtension as NSString, nil)?.takeRetainedValue(),
                    let mimetype = UTTypeCopyPreferredTagWithClass(uti, kUTTagClassMIMEType)?.takeRetainedValue() {
                return mimetype as String
            }'''
    new = ('            #if canImport(MobileCoreServices) || canImport(CoreServices)\n'
           + old + '\n            #endif')
    # Here the old block is deliberately contained within the corrected block.
    if text.count(new) == 1:
        if text.count(old) != 1:
            raise ValueError('Unexpected Swift MIME template')
    elif text.count(old) == 1:
        text = text.replace(old, new)
    else:
        raise ValueError('Unexpected Swift MIME template')
    validation_name = 'OpenAPIClient/Classes/OpenAPIs/Validation.swift'
    validation = root / validation_name
    source = validation.read_text()
    declarations = re.findall(r'public struct (?:Schema)?ValidationError<T: Error & Hashable>: Error', source)
    if len(declarations) != 1:
        raise ValueError('Unexpected Swift validation template')
    source = re.sub(r'\bValidationError\b', 'SchemaValidationError', source)
    path.write_text(text)
    validation.write_text(source)
    return [name, validation_name]
