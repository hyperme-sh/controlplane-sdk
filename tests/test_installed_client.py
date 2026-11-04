"""Exercise the installed generated client without calling a live service."""
import importlib
import pkgutil


def test_every_generated_module_imports():
    import openapi_client
    for module in pkgutil.walk_packages(openapi_client.__path__, openapi_client.__name__ + "."):
        importlib.import_module(module.name)


def test_health_response_roundtrip():
    from openapi_client.models.health_check_response_dto import HealthCheckResponseDto
    result = HealthCheckResponseDto.from_json('{"status":"ok"}')
    assert result.to_dict() == {"status": "ok"}
    assert HealthCheckResponseDto.from_json(result.to_json()) == result


def test_client_serialization():
    from openapi_client import ApiClient, Configuration
    from openapi_client.models.health_check_response_dto import HealthCheckResponseDto
    with ApiClient(Configuration(host="https://sdk.invalid")) as client:
        assert client.sanitize_for_serialization(HealthCheckResponseDto(status="ok")) == {"status": "ok"}
