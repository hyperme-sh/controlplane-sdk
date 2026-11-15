import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test
import org.openapitools.client.models.*

class WalletWireTest {
    private val mapper = jacksonObjectMapper()
    @Test fun proofIsAnObject() {
        val result = mapper.readTree(mapper.writeValueAsString(WalletPaymentSubmitRequest("message", "nonce", "0x1234")))
        assertEquals(setOf("message", "nonce", "signature"), result.fieldNames().asSequence().toSet())
        assertEquals("0x1234", result["signature"].asText())
    }
    @Test fun challengeAndPaymentUseOnlyWireKeys() {
        val challenge = mapper.readTree(mapper.writeValueAsString(WalletPaymentChallengeRequest("0x" + "11".repeat(20), 84532)))
        assertEquals(setOf("address", "chain_id"), challenge.fieldNames().asSequence().toSet())
        val payment = mapper.readTree(mapper.writeValueAsString(WalletPaymentUsdcLeasePaymentCreate(50)))
        assertEquals(50, payment["amount_cents"].asInt())
        assertFalse(payment.has("amountCents"))
    }
    @Test fun nullDepositDetailsRemainObservable() {
        val value: WalletPaymentWalletDepositStatus = mapper.readValue("""{"amount_cents":50,"billing_record_id":"22222222-2222-4222-8222-222222222222","lease_id":"33333333-3333-4333-8333-333333333333","deposit_address":null,"provider_status":null,"settled":false,"status":"pending"}""")
        assertNull(value.depositAddress)
        assertNull(value.providerStatus)
        assertFalse(value.settled)
    }
}
