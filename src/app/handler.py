from fastapi import APIRouter
from app.notificationSender import NotificationSender, NotificationError
from app.push_services.fcm import FCM
from app.push_services.pypush import PyPushWoosh
from app.push_services.pushbullet import PushBulletSender
from app.models import NotifiactionRequest, NotificationResponse

router = APIRouter(prefix='/api/v1/push')
push_services: dict[str: NotificationSender] = {
    "fcm": FCM,
    "pypush": PyPushWoosh,
    "pushbullet": PushBulletSender
}
@router.post(path='/message/')
async def send_push(request: NotifiactionRequest) -> NotificationResponse:
    service: NotificationSender = push_services.get(request.channel_type, None)
    if service:
        try:
            service.send(request.message)
            return NotificationResponse(message = 'Succesfuly sent')
        except NotificationError as notification_error:
            return NotificationResponse(message = 'Failed to sent message')
    return NotificationResponse(message = 'No such push service')
    