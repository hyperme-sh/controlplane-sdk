/**
 * Keycloak OAuth2 helpers (PKCE, device code, client credentials).
 * Configure via env: KEYCLOAK_URL, KEYCLOAK_REALM, KEYCLOAK_CLIENT_ID.
 */

export type WellKnown = {
  authorization_endpoint: string;
  token_endpoint: string;
  device_authorization_endpoint?: string;
};

export async function fetchWellKnown(
  keycloakBase: string,
  realm: string
): Promise<WellKnown> {
  const u = `${keycloakBase.replace(/\/$/, "")}/realms/${realm}/.well-known/openid-configuration`;
  const r = await fetch(u);
  if (!r.ok) throw new Error(`well-known failed: ${r.status}`);
  return r.json() as Promise<WellKnown>;
}

/** RFC 7636 S256 code verifier / challenge (browser: use Web Crypto or pkce-challenge package). */
export async function pkceChallengeS256(verifier: string): Promise<string> {
  const data = new TextEncoder().encode(verifier);
  const digest = await crypto.subtle.digest("SHA-256", data);
  const bytes = new Uint8Array(digest);
  let bin = "";
  bytes.forEach((b) => (bin += String.fromCharCode(b)));
  return btoa(bin).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

export function buildAuthorizeUrl(params: {
  wellKnown: WellKnown;
  clientId: string;
  redirectUri: string;
  state: string;
  codeChallenge: string;
  scope?: string;
}): string {
  const u = new URL(params.wellKnown.authorization_endpoint);
  u.searchParams.set("client_id", params.clientId);
  u.searchParams.set("response_type", "code");
  u.searchParams.set("redirect_uri", params.redirectUri);
  u.searchParams.set("scope", params.scope ?? "openid email profile");
  u.searchParams.set("state", params.state);
  u.searchParams.set("code_challenge_method", "S256");
  u.searchParams.set("code_challenge", params.codeChallenge);
  return u.toString();
}

export async function exchangeCodeForTokens(params: {
  tokenEndpoint: string;
  clientId: string;
  redirectUri: string;
  code: string;
  codeVerifier: string;
}): Promise<Record<string, unknown>> {
  const body = new URLSearchParams({
    grant_type: "authorization_code",
    client_id: params.clientId,
    redirect_uri: params.redirectUri,
    code: params.code,
    code_verifier: params.codeVerifier,
  });
  const r = await fetch(params.tokenEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });
  if (!r.ok) throw new Error(`token exchange failed: ${r.status}`);
  return r.json() as Promise<Record<string, unknown>>;
}

export async function startDeviceCodeFlow(params: {
  deviceEndpoint: string;
  clientId: string;
  scope?: string;
}): Promise<{ device_code: string; user_code: string; verification_uri: string; interval: number }> {
  const body = new URLSearchParams({
    client_id: params.clientId,
    scope: params.scope ?? "openid profile",
  });
  const r = await fetch(params.deviceEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });
  if (!r.ok) throw new Error(`device authorization failed: ${r.status}`);
  return r.json() as Promise<{
    device_code: string;
    user_code: string;
    verification_uri: string;
    interval: number;
  }>;
}

export async function pollDeviceToken(params: {
  tokenEndpoint: string;
  clientId: string;
  deviceCode: string;
}): Promise<Record<string, unknown>> {
  const body = new URLSearchParams({
    grant_type: "urn:ietf:params:oauth:grant-type:device_code",
    client_id: params.clientId,
    device_code: params.deviceCode,
  });
  const r = await fetch(params.tokenEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });
  const j = (await r.json()) as Record<string, unknown>;
  if (!r.ok) throw new Error(String(j.error ?? r.status));
  return j;
}

export async function clientCredentialsToken(params: {
  tokenEndpoint: string;
  clientId: string;
  clientSecret: string;
  scope?: string;
}): Promise<Record<string, unknown>> {
  const body = new URLSearchParams({
    grant_type: "client_credentials",
    client_id: params.clientId,
    client_secret: params.clientSecret,
    scope: params.scope ?? "openid",
  });
  const r = await fetch(params.tokenEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });
  if (!r.ok) throw new Error(`client_credentials failed: ${r.status}`);
  return r.json() as Promise<Record<string, unknown>>;
}

export function apiKeyHeaders(apiKey: string, tenantId: string): Record<string, string> {
  return {
    "X-Api-Key": apiKey,
    "X-Tenant-ID": tenantId,
  };
}
