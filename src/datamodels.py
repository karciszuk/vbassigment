from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Literal

class User(BaseModel):
    user_id: int
    registration_date: date
    age: int = Field(ge=18)
    income: int = Field(ge=0)
    credit_score: int = Field(ge=300, le=850)

class Transaction(BaseModel):
    transaction_id: int = Field(ge=1, le=500000)
    user_id: int = Field(ge=1, le=100000)
    merchant_id: int = Field(ge=1000, le=9999)
    transaction_amount: float = Field(gt=0.0)
    installments_count: Literal[4, 6, 12, 24]
    transaction_date: date

class Installment(BaseModel):
    installment_id: int = Field(ge=1, le=2000000)
    transaction_id: int = Field(ge=1, le=500000)
    installment_number: int = Field(ge=1, le=24)
    scheduled_date: date
    payment_date: Optional[date] = None
    scheduled_amount: float = Field(ge=0.0)
    paid_amount: float = Field(ge=0.0)

class Merchant(BaseModel):
    merchant_id: int = Field(ge=1000, le=9999)
    merchant_name: str
    category: Literal["electronics", "fashion", "home", "sports", "beauty"]
    onboarding_date: date
    partnership_status: Literal["active", "inactive"]