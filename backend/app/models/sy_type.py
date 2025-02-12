from sqlmodel import Field, SQLModel


class SyType(SQLModel):
    name_en: str
    name_la: str | None = None
    description_en: str | None = None
    description_la: str | None = None
    type: str


class SyTypeBase(SyType, table=True):
    __tablename__ = 'sy_type'

    id: int = Field(default=None, primary_key=True)

    # SALARY = "salary"
    # POSITION = "position"
    # GASOLINE = "gasoline"
    # OVERTIME = "overtime"
    # COMMISSION = "commission"
    # BONUS = "bonus"
    # TIP = "tip"
    # ALLOWANCE = "allowance"
    # SEVERANCE = "severance"
    # PROFITSHARING = "profit sharing"
    # ADVANCE = "advance"
