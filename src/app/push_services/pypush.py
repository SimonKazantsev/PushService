from pypushwoosh.client import PushwooshClient
from pypushwoosh.command import CreateTargetedMessageCommand
from pypushwoosh.filter import ApplicationFilter
from app.notificationSender import NotificationSender

class PyPushWoosh(NotificationSender):
    """PushWoosh."""
    @classmethod
    def send(cls):
        """Отправка сообщения."""
        command = CreateTargetedMessageCommand()
        command.auth = "AUTH_TOKEN"
        command.content = 'TEXT'
        command.devices_filter = 'app'

        client = PushwooshClient()
        print(client.invoke(command = command))