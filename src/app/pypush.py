from pypushwoosh.client import PushwooshClient
from pypushwoosh.command import CreateTargetedMessageCommand
from pypushwoosh.filter import ApplicationFilter
from app.notificationSender import NotificationSender

class PyPushWoosh(NotificationSender):
    @classmethod
    def send(cls):
        command = CreateTargetedMessageCommand()
        command.auth = "AUTH_TOKEN"
        command.content = 'TEXT'
        command.devices_filter = 'app'

        client = PushwooshClient()
        print(client.invoke(command = command))