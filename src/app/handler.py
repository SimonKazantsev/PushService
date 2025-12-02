from fastapi import APIRouter
from app.notificationSender import NotificationSender, NotificationError
from app.push_services.fcm import FCM
from app.push_services.pushbullet import PushBulletSender
from app.models import NotificationRequest, NotificationResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix='/api/v1/push')
push_services: dict[str: NotificationSender] = {
    "fcm": FCM,
    "pushbullet": PushBulletSender
}

@router.post(path='/message/')
async def send_push(request: NotificationRequest) -> NotificationResponse:
    service: NotificationSender = push_services.get(request.channel_type, None)
    if service:
        logger.info(msg = 'push service choosed')
        try:
            logger.info(msg = 'try to send message')
            await service.async_send(request.message)
            return NotificationResponse(message = 'Succesfuly sent')
        except NotificationError:
            return NotificationResponse(message = 'Failed to sent message')
    return NotificationResponse(message = 'No such push service')
    