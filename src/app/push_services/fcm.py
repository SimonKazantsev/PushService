from app.notificationSender import NotificationSender
from firebase_admin import credentials

class FCM(NotificationSender):
    """Firebase Cloud Messaging."""
    @classmethod
    def send():
        """Отправка сообщения."""
        try:
            pass
        except Exception as e:
            return False