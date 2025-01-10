from sqlmodel import SQLModel, Field


class PaymentTypes(SQLModel, table=True):
    __tablename__ = 'payment_types'
    id: int = Field(default=None, primary_key=True)
    la_name: str = Field(max_length=50)
    en_name: str = Field(max_length=50)
    description: str = Field(max_length=150)


class DeductionTypes(SQLModel, table=True):
    __tablename__ = 'deduction_types'
    id: int = Field(default=None, primary_key=True)
    la_name: str = Field(max_length=50)
    en_name: str = Field(max_length=50)
    description: str = Field(max_length=150)
