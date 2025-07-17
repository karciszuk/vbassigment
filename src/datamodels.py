from pydantic import BaseModel
from datetime import date
from typing import Optional

class User(BaseModel):
    user_id: int
    registration_date: date
    age: int
    income: int
    credit_score: int

class Transaction(BaseModel):
    transaction_id: int
    user_id: int
    merchant_id: int
    transaction_amount: float
    installments_count: int
    transaction_date: date

class Installment(BaseModel):
    installment_id: int
    transaction_id: int
    installment_number: int
    scheduled_date: date
    payment_date: Optional[date]
    scheduled_amount: float
    paid_amount: float

class Merchant(BaseModel):
    merchant_id: int
    merchant_name: str
    category: str
    onboarding_date: date
    partnership_status: str