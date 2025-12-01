import os
from app.models import Message
from pushbullet import PushBullet
from pushbullet.errors import InvalidKeyError, PushError
from app.notificationSender import NotificationSender, NotificationError

class PushBulletSender(NotificationSender):
    """PushBullet."""
    @classmethod
    def send(cls, message: Message):
        """Отправка сообщения."""
        api_key = os.getenv('PUSHBULLET_API_KEY', None)
        try:
            pb = PushBullet(api_key)
        except InvalidKeyError as publicKeyError:
            raise NotificationError from publicKeyError
        try:
            push = pb.push_note(title = message.title, body = message.body)
        except PushError as pushError:
            raise NotificationError from pushError