from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class HTTPError(BaseModel):
    detail: str

class UserBase(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    is_doctor: Optional[bool] = False

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    appointments: list['Appointment'] = []
    messages: list['Message'] = []
    messages_received: list['Message'] = []
    medical_records: list['MedicalRecord'] = []
    prescriptions: list['Prescription'] = []

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    date_time: datetime
    reason: str
    status: str = 'pending'

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

class MessageBase(BaseModel):
    sender_id: int
    recipient_id: int
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    timestamp: datetime

class MedicalRecordBase(BaseModel):
    patient_id: int
    document: str

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecord(MedicalRecordBase):
    id: int
    timestamp: datetime

class PrescriptionBase(BaseModel):
    patient_id: int
    medication: str
    dosage: str
    instructions: str

class PrescriptionCreate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    id: int
    timestamp: datetime

class BillingBase(BaseModel):
    patient_id: int
    amount: int
    status: str
    insurance_claim_id: Optional[int] = None

class BillingCreate(BillingBase):
    pass

class Billing(BillingBase):
    id: int
    date: datetime

class InsuranceClaimBase(BaseModel):
    patient_id: int
    claim_number: str
    status: str

class InsuranceClaimCreate(InsuranceClaimBase):
    pass

class InsuranceClaim(InsuranceClaimBase):
    id: int
    date_submitted: datetime