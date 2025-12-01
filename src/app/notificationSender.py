from abc import ABC, abstractmethod
from app.models import Message

class NotificationError(Exception):
    pass

class NotificationSender(ABC):
    @classmethod
    @abstractmethod    
    def send(message: Message):
        ...