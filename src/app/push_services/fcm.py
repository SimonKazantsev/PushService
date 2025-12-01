from app.notificationSender import NotificationSender
from firebase_admin import credentials, messaging
import firebase_admin
import os

class FCM(NotificationSender):
    """Firebase Cloud Messaging."""
    cred_path = os.getenv("CRED_PATH", None)
    _initialized = False

    @classmethod
    def initialize(cls, cred_path):
        """Инициализация Firebase, выполняется только один раз."""
        if not cls._initialized:
            try:
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
                print("Firebase initialized successfully.")
                cls._initialized = True
            except FileNotFoundError:
                print(f"Error: Credentials file not found at {cred_path}")
                return False
            except Exception as e:
                print(f"Error initializing Firebase: {e}")
                return False
        return True  

    @classmethod
    def send(cls, registration_token, title, body, data=None):
        """Отправка сообщения."""
        if not cls._initialized:
            print("Firebase not initialized. Call FCM.initialize() first.")
            cls.initialize(cred_path = cls.cred_path)
            return False

        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            data=data,
            token=registration_token,
        )

        try:
            response = messaging.send(message)
            print(f"Successfully sent message: {response}")
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False