from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import PrescriptionCreate, PrescriptionResponse
from ..models import Prescription

router = APIRouter(prefix='/api/prescriptions', tags=['Prescriptions'])

@router.post('/', response_model=PrescriptionResponse)
def create_prescription(prescription: PrescriptionCreate, db: Session = Depends(get_db)):
    new_prescription = Prescription(**prescription.dict())
    db.add(new_prescription)
    db.commit()
    db.refresh(new_prescription)
    return new_prescription
