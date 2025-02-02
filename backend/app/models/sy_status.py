from enum import Enum


class SyStatus(Enum):
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
