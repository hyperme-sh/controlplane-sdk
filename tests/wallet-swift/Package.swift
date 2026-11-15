// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "WalletWireContracts",
    dependencies: [
        .package(name: "OpenAPIClient", path: "../../sdk/rest/swift5"),
        .package(url: "https://github.com/Flight-School/AnyCodable", .exact("0.6.1")),
    ],
    targets: [
        .testTarget(name: "WalletWireTests", dependencies: [
            .product(name: "OpenAPIClient", package: "OpenAPIClient"),
        ]),
    ]
)
