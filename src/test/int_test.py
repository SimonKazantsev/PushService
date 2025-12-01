import pytest

def test_send_push_succes(client):
    response = client.post('/api/v1/push/message/')
    assert response.status_code == 200
