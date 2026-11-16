import Foundation
import XCTest
import OpenAPIClient

final class WalletWireTests: XCTestCase {
    func object<T: Encodable>(_ value: T) throws -> [String: Any] {
        return try XCTUnwrap(JSONSerialization.jsonObject(with: JSONEncoder().encode(value)) as? [String: Any])
    }

    func testProofUsesOnlyContractKeys() throws {
        let body = try object(WalletPaymentSubmitRequest(message: "sign this", nonce: String(repeating: "a", count: 64), signature: "0x1234"))
        XCTAssertEqual(Set(body.keys), Set(["message", "nonce", "signature"]))
        XCTAssertEqual(body["signature"] as? String, "0x1234")
    }

    func testPendingDepositPreservesExplicitNulls() throws {
        let data = Data(#"{"amount_cents":50,"billing_record_id":"22222222-2222-4222-8222-222222222222","lease_id":"33333333-3333-4333-8333-333333333333","deposit_address":null,"provider_status":null,"settled":false,"status":"pending"}"#.utf8)
        let value = try JSONDecoder().decode(WalletPaymentWalletDepositStatus.self, from: data)
        XCTAssertNil(value.depositAddress)
        XCTAssertNil(value.providerStatus)
        XCTAssertFalse(value.settled)
        let body = try object(value)
        XCTAssertTrue(body["deposit_address"] is NSNull)
        XCTAssertTrue(body["provider_status"] is NSNull)
        XCTAssertEqual(body["amount_cents"] as? Int, 50)
        XCTAssertNil(body["amountCents"])
    }

    func testServerValidationErrorRemainsDecodable() throws {
        let data = Data(#"{"detail":[{"loc":["body"],"msg":"invalid input","type":"value_error"}]}"#.utf8)
        let value = try JSONDecoder().decode(HTTPValidationError.self, from: data)
        XCTAssertEqual(value.detail?.first?.msg, "invalid input")
    }

    func testIncompleteDepositCannotBecomeConfirmed() {
        let data = Data(#"{"status":"confirmed","settled":true}"#.utf8)
        XCTAssertThrowsError(try JSONDecoder().decode(WalletPaymentWalletDepositStatus.self, from: data))
    }
}
