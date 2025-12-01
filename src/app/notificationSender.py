from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @classmethod
    @abstractmethod    
    def send():
        ...