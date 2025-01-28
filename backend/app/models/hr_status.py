from enum import Enum


class InOutStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    UPDATED = "updated"
    DELETED = "deleted"
    COMPLETED = "completed"
    DRAFT = "draft"
    ONPROGRESS = " onprogress"
    SUBMITTED = "submitted"
    ACTIVE = "active"
    INITIATED = "initiated"
    INACTIVE = "inactive"
