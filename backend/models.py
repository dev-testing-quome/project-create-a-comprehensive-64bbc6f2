import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    is_doctor = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    appointments = relationship("Appointment", back_populates="patient")
    messages = relationship("Message", back_populates="sender", foreign_keys="Message.sender_id")
    messages_received = relationship("Message", back_populates="recipient", foreign_keys="Message.recipient_id")
    medical_records = relationship("MedicalRecord", back_populates="patient")
    prescriptions = relationship("Prescription", back_populates="patient")

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    doctor_id = Column(Integer, ForeignKey("users.id"))
    date_time = Column(DateTime)
    reason = Column(Text)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    patient = relationship("User", back_populates="appointments", foreign_keys=[patient_id])
    doctor = relationship("User", back_populates="appointments", foreign_keys=[doctor_id])

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    sender = relationship("User", back_populates="messages", foreign_keys=[sender_id])
    recipient = relationship("User", back_populates="messages_received", foreign_keys=[recipient_id])

class MedicalRecord(Base):
    __tablename__ = "medical_records"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    document = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    patient = relationship("User", back_populates="medical_records")

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    medication = Column(String)
    dosage = Column(String)
    instructions = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    patient = relationship("User", back_populates="prescriptions")

class Billing(Base):
    __tablename__ = "billing"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String) #e.g., 'paid', 'pending', 'unpaid'
    insurance_claim_id = Column(Integer, ForeignKey("insurance_claims.id"))
    insurance_claim = relationship("InsuranceClaim", back_populates="billing")

class InsuranceClaim(Base):
    __tablename__ = "insurance_claims"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    claim_number = Column(String)
    date_submitted = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String)
    billing = relationship("Billing", back_populates="insurance_claim")