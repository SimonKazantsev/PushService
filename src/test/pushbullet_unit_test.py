import pytest
from pytest_mock import MockerFixture
from unittest.mock import MagicMock
from app.notificationSender import NotificationError
from app.push_services.pushbullet import PushBulletSender
from pushbullet.errors import InvalidKeyError, PushError

def test_pushbullet_send_correct(message, mocker: MockerFixture):
    pushbullet_mock = MagicMock()
    mocker.patch(
    'app.push_services.pushbullet.PushBullet',
    return_value = pushbullet_mock)
    pushbullet_mock.push_note.return_value = True
    response = PushBulletSender.send(message = message)
    assert response == None

def test_pushbullet_send_wrong_api_key(message, monkeypatch):
    monkeypatch.setenv("PUSHBULLET_API_KEY", "INVALID_KEY")
    with pytest.raises(NotificationError) as test_error:
        PushBulletSender.send(message = message)
    assert isinstance(test_error.value.__cause__, InvalidKeyError)

def test_pushbullet_send_push_error(message, mocker: MockerFixture):
    pushbullet_mock = MagicMock()
    mocker.patch(
    'app.push_services.pushbullet.PushBullet',
    return_value = pushbullet_mock)
    pushbullet_mock.push_note.side_effect = PushError
    with pytest.raises(NotificationError) as test_error:
        PushBulletSender.send(message = message)
    assert isinstance(test_error.value.__cause__, PushError)

