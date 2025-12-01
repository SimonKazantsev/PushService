from abc import ABC, abstractmethod

class NotificationError(Exception):
    pass

class NotificationSender(ABC):
    @classmethod
    @abstractmethod    
    def send():
        ...