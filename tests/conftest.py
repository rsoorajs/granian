import asyncio
import multiprocessing as mp
import socket
from contextlib import asynccontextmanager, closing
from functools import partial
from pathlib import Path

import pytest

from granian import Granian


def _serve(**kwargs):
    server = Granian(f'tests.apps.{kwargs["interface"]}:app', **kwargs)
    server.serve()


@asynccontextmanager
async def _server(interface, port, runtime_mode, ws=True, tls=False, task_impl='asyncio', static_mount=False):
    certs_path = Path.cwd() / 'tests' / 'fixtures' / 'tls'
    kwargs = {
        'interface': interface,
        'port': port,
        'loop': 'asyncio',
        'blocking_threads': 1,
        'runtime_mode': runtime_mode,
        'task_impl': task_impl,
        'websockets': ws,
    }
    if tls:
        if tls == 'private':
            kwargs['ssl_cert'] = certs_path / 'pcert.pem'
            kwargs['ssl_key'] = certs_path / 'pkey.pem'
            kwargs['ssl_key_password'] = 'foobar'  # noqa: S105
        else:
            kwargs['ssl_cert'] = certs_path / 'cert.pem'
            kwargs['ssl_key'] = certs_path / 'key.pem'
    if static_mount:
        kwargs['static_path_mount'] = Path.cwd() / 'tests' / 'fixtures'

    succeeded, spawn_failures = False, 0
    while spawn_failures < 3:
        proc = mp.get_context('spawn').Process(target=_serve, kwargs=kwargs)
        proc.start()

        conn_failures = 0
        while conn_failures < 3:
            try:
                await asyncio.sleep(1.5)
                sock = socket.create_connection(('127.0.0.1', port), timeout=1)
                sock.close()
                succeeded = True
                break
            except Exception:
                conn_failures += 1
        if succeeded:
            break

        proc.terminate()
        proc.join(timeout=2)
        if proc.is_alive():
            proc.kill()
        spawn_failures += 1

    if not succeeded:
        raise RuntimeError('Cannot bind server')

    try:
        yield port
    finally:
        proc.terminate()
        proc.join(timeout=2)
        if proc.is_alive():
            proc.kill()


@pytest.fixture(scope='function')
def server_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(('localhost', 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return sock.getsockname()[1]


@pytest.fixture(scope='function')
def asgi_server(server_port, **extras):
    return partial(_server, 'asgi', server_port, **extras)


@pytest.fixture(scope='function')
def rsgi_server(server_port, **extras):
    return partial(_server, 'rsgi', server_port, **extras)


@pytest.fixture(scope='function')
def wsgi_server(server_port):
    return partial(_server, 'wsgi', server_port)


@pytest.fixture(scope='function')
def server(server_port, request):
    return partial(_server, request.param, server_port)


@pytest.fixture(scope='function')
def server_tls(server_port, request):
    return partial(_server, request.param, server_port, tls=True)


@pytest.fixture(scope='function')
def server_static_files(server_port, request):
    return partial(_server, request.param, server_port, static_mount=True)
