"""Keycloak OAuth2 helpers (PKCE, device code, client credentials) — no OpenAPI."""

from __future__ import annotations

import json
import secrets
import urllib.parse
from typing import Any

import httpx


async def fetch_well_known(keycloak_base: str, realm: str) -> dict[str, Any]:
    base = keycloak_base.rstrip("/")
    url = f"{base}/realms/{realm}/.well-known/openid-configuration"
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.get(url)
        r.raise_for_status()
        return r.json()


def pkce_verifier() -> str:
    return secrets.token_urlsafe(64)


def build_authorize_url(
    *,
    authorization_endpoint: str,
    client_id: str,
    redirect_uri: str,
    state: str,
    code_challenge: str,
    scope: str = "openid email profile",
) -> str:
    q = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "scope": scope,
            "state": state,
            "code_challenge_method": "S256",
            "code_challenge": code_challenge,
        }
    )
    return f"{authorization_endpoint}?{q}"


async def exchange_code_for_tokens(
    *,
    token_endpoint: str,
    client_id: str,
    redirect_uri: str,
    code: str,
    code_verifier: str,
) -> dict[str, Any]:
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code": code,
        "code_verifier": code_verifier,
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.post(
            token_endpoint,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        r.raise_for_status()
        return r.json()


async def client_credentials_token(
    *,
    token_endpoint: str,
    client_id: str,
    client_secret: str,
    scope: str = "openid",
) -> dict[str, Any]:
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.post(
            token_endpoint,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        r.raise_for_status()
        return r.json()


async def start_device_code_flow(
    *,
    device_endpoint: str,
    client_id: str,
    scope: str = "openid profile",
) -> dict[str, Any]:
    data = {"client_id": client_id, "scope": scope}
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.post(
            device_endpoint,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        r.raise_for_status()
        return r.json()


async def poll_device_token(
    *,
    token_endpoint: str,
    client_id: str,
    device_code: str,
) -> dict[str, Any]:
    data = {
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        "client_id": client_id,
        "device_code": device_code,
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.post(
            token_endpoint,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        return r.json()


def api_key_headers(*, api_key: str, tenant_id: str) -> dict[str, str]:
    return {"X-Api-Key": api_key, "X-Tenant-ID": tenant_id}
