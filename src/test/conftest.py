import pytest
from fastapi.testclient import TestClient
from system.service import app

@pytest.fixture
def client():
    return TestClient(app = app)