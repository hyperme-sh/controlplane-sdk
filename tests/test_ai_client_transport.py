"""Installed clients send real loopback requests; the HTTP server is a contract fixture."""

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

from openapi_client import (
    AIApi,
    AiApi,
    AIUsageApi,
    ApiClient,
    Configuration,
    InferenceRequest,
)


def test_inference_and_both_usage_names_share_the_wire_contract():
    requests = []
    inference = {
        "inference_id": "sample-id",
        "text": "answer",
        "model": "test",
        "input_tokens": 3,
        "output_tokens": 5,
        "cost_usd": "0.01",
    }
    record = {
        "id": "sample-id",
        "created_at": "2026-11-04T00:00:00Z",
        "user_id": "user-id",
        "model": "test",
        "input_tokens": 3,
        "output_tokens": 5,
        "cost_usd": "0.01",
        "billing_mode": "none",
        "budget_id": None,
    }

    class Handler(BaseHTTPRequestHandler):
        def handle_request(self):
            parsed = urlsplit(self.path)
            body = (
                json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                if self.command == "POST"
                else None
            )
            requests.append(
                (
                    self.command,
                    parsed.path,
                    parse_qs(parsed.query),
                    dict(self.headers),
                    body,
                )
            )
            if parsed.path == "/api/v1/ai/inference":
                result = inference
            elif parsed.path == "/api/v1/ai/usage/history":
                result = {"items": [record], "total": 1, "limit": 7, "offset": 0}
            elif parsed.path == "/api/v1/ai/usage/summary":
                result = {
                    "total_cost_usd": "0.01",
                    "total_input_tokens": 3,
                    "total_output_tokens": 5,
                }
            else:
                self.send_error(404)
                return
            encoded = json.dumps(result).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

        do_GET = handle_request
        do_POST = handle_request

        def log_message(self, *_args):
            pass

    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with ApiClient(
                Configuration(host=f"http://127.0.0.1:{server.server_port}")
            ) as client:
                client.default_headers.update(
                    {"Authorization": "Bearer fixture", "X-Tenant-ID": "fixture-tenant"}
                )
                result = AIApi(client).inference_api_v1_ai_inference_post(
                    InferenceRequest(prompt="hello", model="test"), _request_timeout=5
                )
                history = AIUsageApi(client).api_v1_ai_usage_history_get(
                    limit=7, _request_timeout=5
                )
                summary = AiApi(client).api_v1_ai_usage_summary_get(_request_timeout=5)
                assert result.inference_id == history.items[0].id == "sample-id"
                assert (
                    summary.total_input_tokens == 3 and summary.total_output_tokens == 5
                )
                assert AiApi is AIUsageApi
        finally:
            server.shutdown()
            thread.join(timeout=5)
    assert len(requests) == 3
    assert requests[0][4]["prompt"] == "hello"
    assert requests[1][2] == {"limit": ["7"]}
    for request in requests:
        assert request[3]["Authorization"] == "Bearer fixture"
        assert request[3]["X-Tenant-ID"] == "fixture-tenant"
