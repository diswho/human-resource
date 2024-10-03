from sqlmodel import SQLModel, Field


class AttDayTypeBase(SQLModel):
    dt_code: int | None = None
    dt_desc: str | None = None
    export_code: str | None = None
    sign: str | None = None


class AttDayType(AttDayTypeBase, table=True):
    __tablename__ = "att_DayType"
    id: int | None = Field(default=None, primary_key=True)


class AttDayTypeCreate(AttDayTypeBase):
    pass


class AttDayTypeUpdate(AttDayTypeBase):
    dt_code: int | None = None
    dt_desc: str | None = None
    export_code: str | None = None
    sign: str | None = None
