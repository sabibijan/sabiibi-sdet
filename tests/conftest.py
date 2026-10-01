"""Shared fixtures: pytest loads this file automatically before any test."""
import functools
import http.server
import os
import threading
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def web_base_url():
    """Serve ./site on http://127.0.0.1:4173 for the whole test run,
    or use WEB_BASE_URL (e.g. your live Cloudflare site) if it's set."""
    live = os.getenv("WEB_BASE_URL")
    if live:
        yield live.rstrip("/")
        return
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT / "site"))
    handler.log_message = lambda *args, **kwargs: None      # keep the output quiet
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 4173), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield "http://127.0.0.1:4173"          # everything after yield is clean-up
    server.shutdown()


@pytest.fixture(scope="session")
def homepage_html(web_base_url) -> str:
    """Download the home page once and share it with every test that asks for it."""
    from urllib.request import urlopen
    with urlopen(web_base_url) as response:
        assert response.status == 200
        return response.read().decode("utf-8")


@pytest.fixture(scope="session")
def base_url(web_base_url):
    """pytest-playwright uses this, so page.goto("/") opens the home page."""
    return web_base_url