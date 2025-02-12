from sqlmodel import Field, SQLModel


class SyStatus(SQLModel):
    name_en: str
    name_la: str | None = None
    description_en: str | None = None
    description_la: str | None = None


class SyStatusBase(SyStatus, table=True):
    __tablename__ = 'sy_status'

    id: int = Field(default=None, primary_key=True)
    # PENDING = "pending"
    # APPROVED = "approved"
    # REJECTED = "rejected"
    # CANCELLED = "cancelled"
    # UPDATED = "updated"
    # DELETED = "deleted"
    # COMPLETED = "completed"
    # DRAFT = "draft"
    # ONPROGRESS = " onprogress"
    # SUBMITTED = "submitted"
    # ACTIVE = "active"
    # INITIATED = "initiated"
    # INACTIVE = "inactive"
