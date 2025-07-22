from pydantic import BaseModel
from datetime import date
from typing import ClassVar


class User(BaseModel):
    table_name: ClassVar[str] = "users"
    user_id: int
    registration_date: date
    age: int
    income: int
    credit_score: int


class Transaction(BaseModel):
    table_name: ClassVar[str] = "transaction"
    transaction_id: int
    user_id: int
    merchant_id: int
    transaction_amount: float
    installments_count: int
    transaction_date: date


class Installment(BaseModel):
    table_name: ClassVar[str] = "installments"
    installment_id: int
    transaction_id: int
    installment_number: int
    scheduled_date: date
    payment_date: date
    scheduled_amount: float
    paid_amount: float


class Merchant(BaseModel):
    table_name: ClassVar[str] = "merchant"
    merchant_id: int
    merchant_name: str
    category: str
    onboarding_date: date
    partnership_status: str
