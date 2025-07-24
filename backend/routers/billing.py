from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import BillingCreate, BillingResponse
from ..models import Billing

router = APIRouter(prefix='/api/billing', tags=['Billing'])

@router.post('/', response_model=BillingResponse)
def create_billing_record(billing: BillingCreate, db: Session = Depends(get_db)):
    new_billing_record = Billing(**billing.dict())
    db.add(new_billing_record)
    db.commit()
    db.refresh(new_billing_record)
    return new_billing_record
