from typing import Any
from app.models.att_day_summary import AttDaySummariesPublic, AttDaySummary, AttDaySummaryPublic
from fastapi import APIRouter
from app.api.deps import SessionDep
from sqlmodel import select, func

router = APIRouter()


@router.get("/", response_model=AttDaySummariesPublic)
def get_attendances(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    count_statement = select(func.count()).select_from(AttDaySummary)
    count = session.exec(count_statement).one()
    statement = select(AttDaySummary).offset(skip).limit(limit)
    attendances = session.exec(statement).all()
    return AttDaySummariesPublic(data=attendances, count=count)
