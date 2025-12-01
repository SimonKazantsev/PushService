from fastapi import APIRouter
from app.push_services.pypush import PyPushWoosh
from app.push_services.pushbullet import PushBulletSender

router = APIRouter(prefix='/api/v1/push')

@router.post(path='/message/')
async def send_push():
    try:
        PushBulletSender.send()
    except Exception as e:
        raise e
    return {"message": "hello!"}