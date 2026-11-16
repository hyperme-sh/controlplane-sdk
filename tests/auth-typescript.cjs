const assert = require('node:assert/strict');
const path = require('node:path');
const auth = require(path.resolve(process.argv[2], 'keycloakAuth.js'));
(async () => {
  assert.equal(await auth.pkceChallengeS256('dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk'), 'E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM');
  const u = new URL(auth.buildAuthorizeUrl({wellKnown:{authorization_endpoint:'https://id.example/auth',token_endpoint:'https://id.example/token'},clientId:'public',redirectUri:'https://app.example/cb?a=1',state:'s + &',codeChallenge:'challenge'}));
  assert.equal(u.searchParams.get('state'), 's + &');
  assert.equal(u.searchParams.get('code_challenge_method'), 'S256');
  assert.deepEqual(auth.apiKeyHeaders('key','tenant'), {'X-Api-Key':'key','X-Tenant-ID':'tenant'});
  let requests = [];
  global.fetch = async (url, options={}) => { requests.push({url,options}); return new Response(JSON.stringify({access_token:'unit-token',token_endpoint:'https://id.example/token'}),{status:200}); };
  await auth.fetchWellKnown('https://id.example/','controlplane');
  assert.equal(requests.at(-1).url,'https://id.example/realms/controlplane/.well-known/openid-configuration');
  await auth.exchangeCodeForTokens({tokenEndpoint:'https://id.example/token',clientId:'public',redirectUri:'https://app.example/cb',code:'code+',codeVerifier:'verifier'});
  assert.equal(requests.at(-1).options.body.get('code'),'code+');
  assert.equal(requests.at(-1).options.body.get('code_verifier'),'verifier');
  assert.equal(requests.at(-1).options.body.has('client_secret'),false);
  await auth.clientCredentialsToken({tokenEndpoint:'https://id.example/token',clientId:'server',clientSecret:'unit-secret'});
  assert.equal(requests.at(-1).options.body.get('grant_type'),'client_credentials');
  await auth.startDeviceCodeFlow({deviceEndpoint:'https://id.example/device',clientId:'public'});
  assert.equal(requests.at(-1).options.body.has('client_secret'),false);
  const poll = () => auth.pollDeviceToken({tokenEndpoint:'https://id.example/token',clientId:'public',deviceCode:'device'});
  await poll();
  assert.equal(requests.at(-1).options.body.get('grant_type'),'urn:ietf:params:oauth:grant-type:device_code');
  for (const [status,error] of [[400,'authorization_pending'],[400,'slow_down'],[403,'access_denied'],[503,'unavailable']]) {
    global.fetch = async () => new Response(JSON.stringify({error}),{status});
    await assert.rejects(poll,new RegExp(error));
  }
  console.log('TypeScript PKCE, grants, scope headers and failed poll contracts passed');
})().catch(error => { console.error(error); process.exitCode=1; });
