import pytest
from pytest_mock import MockerFixture
from app.fcm import FCM

def test_send_message_FCM():
    response = FCM.send()
    assert response == "Message sent succesfuly!"

def test_send_message_FCM_error(mocker: MockerFixture):
    mocker.patch('app.fcm.FCM.send', side_effect = Exception)
    response = FCM.send()
    assert response == "Failed to sent Message!"