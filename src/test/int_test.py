import pytest
from pytest_mock import MockerFixture
from unittest.mock import AsyncMock, MagicMock
from app.notificationSender import NotificationError

def test_send_push_succes(client, mocker: MockerFixture):
    json = {
        "channel_type": "pushbullet",
        "message": {
            "title": "Fastapi",
            "body": "It Works!"
        }
    }
    push_services = MagicMock()
    push_service = AsyncMock()
    mocker.patch('app.handler.push_services', new = push_services)
    push_services.get.return_value = push_service
    push_service.async_send.return_value = True
    response = client.post('/api/v1/push/message/', json = json)
    assert response.status_code == 200
    assert response.json() == {'message': "Succesfuly sent"}

def test_send_push_wrong_service(client, mocker: MockerFixture):
    json = {
        "channel_type": "wrong_service",
        "message": {
            "title": "Fastapi",
            "body": "It Works!"
        }
    }
    push_services = MagicMock()
    mocker.patch('app.handler.push_services', new = push_services)
    push_services.get.return_value = None
    response = client.post('/api/v1/push/message/', json = json)
    assert response.json() == {"message": "No such push service"}

def test_send_push_failed(client, mocker: MockerFixture):
    json = {
        "channel_type": "correct_service",
        "message": {
            "title": "Fastapi",
            "body": "It Works!"
        }
    }
    push_services = MagicMock()
    push_service = AsyncMock()
    mocker.patch('app.handler.push_services', new = push_services)
    push_services.get.return_value = push_service
    push_service.async_send.side_effect = NotificationError
    
    response = client.post('/api/v1/push/message/', json = json)
    
    assert response.json() == {"message": "Failed to sent message"}