from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import MedicalRecordCreate, MedicalRecordResponse
from ..models import MedicalRecord

router = APIRouter(prefix='/api/medical_records', tags=['Medical Records'])

@router.post('/', response_model=MedicalRecordResponse)
def create_medical_record(medical_record: MedicalRecordCreate, db: Session = Depends(get_db)):
    new_medical_record = MedicalRecord(**medical_record.dict())
    db.add(new_medical_record)
    db.commit()
    db.refresh(new_medical_record)
    return new_medical_record
