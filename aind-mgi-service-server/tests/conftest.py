"""Set up fixtures to be used across all test modules."""

import json
import os
from pathlib import Path
from typing import Any, Generator
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from httpx import URL, AsyncClient
from pydantic import RedisDsn
from pytest_httpx import HTTPXMock

from aind_mgi_service_server.configs import settings
from aind_mgi_service_server.main import app

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

patch(
    "fastapi_cache.decorator.cache", lambda *args, **kwargs: lambda f: f
).start()


@pytest.fixture(scope="function")
async def mock_async_client_get_pvalb(httpx_mock: HTTPXMock) -> AsyncClient:
    """Generate an async session for testing."""

    with open(RESOURCES_DIR / "example_response.json") as f:
        contents = json.load(f)

    base_url = "http://example.com/quicksearch/alleleBucket"
    base_params = {
        "queryType": "exactPhrase",
        "submit": "Quick+Search",
    }
    params = {"query": "Parvalbumin-IRES-Cre"} | base_params
    httpx_mock.add_response(url=URL(base_url, params=params), json=contents)
    return AsyncClient(base_url="http://example.com")


@pytest.fixture(scope="function")
async def mock_async_client_get_nothing(httpx_mock: HTTPXMock) -> AsyncClient:
    """Generate an async session for testing."""

    base_url = "http://example.com/quicksearch/alleleBucket"
    base_params = {
        "queryType": "exactPhrase",
        "submit": "Quick+Search",
    }
    params = {"query": "NOTHING"} | base_params
    httpx_mock.add_response(
        url=URL(base_url, params=params),
        json={"summaryRows": [], "totalCount": 0, "meta": None},
    )
    return AsyncClient(base_url="http://example.com")


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def client_with_redis() -> Generator[TestClient, Any, None]:
    """Creating a client when settings have a redis_url. Only used in one test
    to verify the lifespan method in main is called correctly."""

    # Import moved to be able to mock cache
    from aind_mgi_service_server.main import app

    settings_with_redis = settings.model_copy(
        update={"redis_url": RedisDsn("redis://example.com:1234")}, deep=True
    )
    with (
        patch(
            "aind_mgi_service_server.main.settings",
            return_value=settings_with_redis,
        ),
        patch("aind_mgi_service_server.main.from_url", return_value=None),
        patch(
            "aind_mgi_service_server.main.RedisBackend",
            return_value=None,
        ),
    ):
        with TestClient(app) as c:
            yield c
