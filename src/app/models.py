from pydantic import BaseModel

class Message(BaseModel):
    title: str
    body: str

class NotifiactionRequest(BaseModel):
    channel_type: str
    message: Message

class NotificationResponse(BaseModel):
    message: str