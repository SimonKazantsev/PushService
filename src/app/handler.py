from fastapi import APIRouter
from app.pypush import PyPushWoosh
from app.pushbullet import PushBulletSender

router = APIRouter(prefix='/api/v1/push')

@router.post(path='/message/')
async def send_push():
    try:
        PushBulletSender.send()
    except Exception as e:
        raise e
    return {"message": "hello!"}