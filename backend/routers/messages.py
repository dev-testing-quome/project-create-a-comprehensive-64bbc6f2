from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import MessageCreate, MessageResponse
from ..models import Message

router = APIRouter(prefix='/api/messages', tags=['Messages'])

@router.post('/', response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    new_message = Message(**message.dict())
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message
