from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import MedicalRecord
from ..schemas import MedicalRecord, MedicalRecordCreate

router = APIRouter(prefix="/api/medical_records", tags=["Medical Records"])

@router.post("", status_code=status.HTTP_201_CREATED, response_model=MedicalRecord)
def create_medical_record(medical_record: MedicalRecordCreate, db: Session = Depends(get_db)):
    # Add medical record creation logic here
    pass

@router.get("/{medical_record_id}", response_model=MedicalRecord)
def get_medical_record(medical_record_id: int, db: Session = Depends(get_db)):
    # Add medical record retrieval logic here
    pass