from sqlmodel import SQLModel, Field
from decimal import Decimal

# AttStatisticItem


class AttStatisticItemBase(SQLModel):
    item_code: int
    item_desc: str | None = None
    item_type: int | None = None
    export_code: str | None = None
    isDeleted: bool | None = None
    sign: str | None = None
    yearlyLimit: Decimal | None = None
    item_Mode: int | None = None
    ColorValue: int | None = None


class AttStatisticItemCreate(AttStatisticItemBase):
    pass


class AttStatisticItemUpdate(AttStatisticItemBase):
    item_code: int | None = None

# Set table name and unique constraint


class AttStatisticItem(AttStatisticItemBase, table=True):
    __tablename__ = "att_StatisticItem"
    id: int | None = Field(default=None, primary_key=True)
