from pydantic import BaseModel


class NotifiactionRequest(BaseModel):
    channel_type: str

class NotificationResponse(BaseModel):
    message: str