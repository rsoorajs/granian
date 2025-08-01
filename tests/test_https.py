import json
import pathlib
import ssl

import httpx
import pytest
import websockets


@pytest.mark.asyncio
@pytest.mark.parametrize('server_tls', ['asgi', 'rsgi', 'wsgi'], indirect=True)
@pytest.mark.parametrize('runtime_mode', ['mt', 'st'])
async def test_http_scope(server_tls, runtime_mode):
    async with server_tls(runtime_mode, ws=False) as port:
        res = httpx.get(f'https://localhost:{port}/info?test=true', verify=False)

    assert res.status_code == 200
    data = res.json()
    assert data['scheme'] == 'https'


@pytest.mark.asyncio
@pytest.mark.parametrize('runtime_mode', ['mt', 'st'])
async def test_asgi_ws_scope(asgi_server, runtime_mode):
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    localhost_pem = pathlib.Path.cwd() / 'tests' / 'fixtures' / 'tls' / 'cert.pem'
    ssl_context.load_verify_locations(str(localhost_pem))

    async with asgi_server(runtime_mode, tls=True) as port:
        async with websockets.connect(f'wss://localhost:{port}/ws_info?test=true', ssl=ssl_context) as ws:
            res = await ws.recv()

    data = json.loads(res)
    assert data['scheme'] == 'wss'


@pytest.mark.asyncio
@pytest.mark.parametrize('runtime_mode', ['mt', 'st'])
async def test_rsgi_ws_scope(rsgi_server, runtime_mode):
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    localhost_pem = pathlib.Path.cwd() / 'tests' / 'fixtures' / 'tls' / 'cert.pem'
    ssl_context.load_verify_locations(str(localhost_pem))

    async with rsgi_server(runtime_mode, tls=True) as port:
        async with websockets.connect(f'wss://localhost:{port}/ws_info?test=true', ssl=ssl_context) as ws:
            res = await ws.recv()

    data = json.loads(res)
    assert data['scheme'] == 'https'


@pytest.mark.asyncio
async def test_tls_encrypted_key(rsgi_server):
    async with rsgi_server('st', ws=False, tls='priv') as port:
        res = httpx.get(f'https://localhost:{port}/info?test=true', verify=False)

    assert res.status_code == 200
    data = res.json()
    assert data['scheme'] == 'https'
