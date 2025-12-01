import os
from pushbullet import PushBullet
from pushbullet.errors import InvalidKeyError, PushError
from app.notificationSender import NotificationSender

class PushBulletSender(NotificationSender):
    @classmethod
    def send(cls):
        api_key = os.getenv('PUSHBULLET_API_KEY', None)
        try:
            pb = PushBullet(api_key)
        except InvalidKeyError as publicKeyError:
            raise InvalidKeyError from publicKeyError
        try:
            push = pb.push_note("Hello Title", "Hello text")
        except PushError as pushError:
            raise PushError