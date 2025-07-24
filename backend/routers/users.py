from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserCreate, UserResponse
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash

router = APIRouter(prefix='/api/users', tags=['Users'])

@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = generate_password_hash(user.password)
    new_user = User(username=user.username, password=hashed_password, email=user.email, first_name=user.first_name, last_name=user.last_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user
