"""Set up fixtures to be used across all test modules."""

import json
import os
from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient

from aind_mgi_service_server.main import app

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


@pytest.fixture()
def mock_get_example_response(mocker):
    """Mock example response"""
    with open(RESOURCES_DIR / "example_response.json") as f:
        contents = json.load(f)

    # Create a mock response that behaves like httpx.Response
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = contents
    mock_response.raise_for_status.return_value = None

    # Patch the httpx.AsyncClient.get method
    mock_get = mocker.patch(
        "httpx.AsyncClient.get", return_value=mock_response
    )
    return mock_get


@pytest.fixture()
def mock_get_empty_response(mocker):
    """Mock empty string response"""

    # Create a mock response that behaves like httpx.Response
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "summaryRows": [],
        "totalCount": 0,
        "meta": None,
    }
    mock_response.raise_for_status.return_value = None

    # Patch the httpx.AsyncClient.get method
    mock_get = mocker.patch(
        "httpx.AsyncClient.get", return_value=mock_response
    )
    return mock_get


@pytest.fixture()
async def get_test_session():
    """Generate an async session for testing."""
    async with httpx.AsyncClient(base_url="http://example.com") as session:
        yield session


@pytest.fixture(scope="session")
def client():
    """Creating a client for testing purposes."""
    with TestClient(app) as c:
        yield c
