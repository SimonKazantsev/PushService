from app.notificationSender import NotificationSender
from firebase_admin import credentials

class FCM(NotificationSender):
    @classmethod
    def send():
        try:
            pass
        except Exception as e:
            return False