import pytest
from fastapi.testclient import TestClient

from fastzero.main import app


@pytest.fixture
def client():
    return TestClient(app)
