from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime

class AppointmentCreate(BaseModel):
    patient_id: int
    provider_id: int
    date_time: datetime
    description: str

class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    provider_id: int
    date_time: datetime
    description: str
    created_at: datetime
    updated_at: datetime

class MessageCreate(BaseModel):
    sender_id: int
    recipient_id: int
    content: str

class MessageResponse(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    timestamp: datetime

class MedicalRecordCreate(BaseModel):
    patient_id: int
    document: str
    description: str

class MedicalRecordResponse(BaseModel):
    id: int
    patient_id: int
    document: str
    description: str
    created_at: datetime
    updated_at: datetime

class PrescriptionCreate(BaseModel):
    patient_id: int
    medication: str
    dosage: str
    instructions: str

class PrescriptionResponse(BaseModel):
    id: int
    patient_id: int
    medication: str
    dosage: str
    instructions: str
    date_prescribed: datetime
    created_at: datetime
    updated_at: datetime

class BillingCreate(BaseModel):
    patient_id: int
    service: str
    amount: int
    insurance_claim_status: Optional[str] = None

class BillingResponse(BaseModel):
    id: int
    patient_id: int
    service: str
    amount: int
    date: datetime
    insurance_claim_status: Optional[str]
    created_at: datetime
    updated_at: datetime
