from collections.abc import Generator
from typing import Annotated, Any, Dict, List, Tuple

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from sqlmodel import Session, select

from app.core import security
from app.core.config import settings
from app.core.db import engine
from app.models.hr_department import HRDepartment
from app.models.models import TokenPayload
from app.models.user import User

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]


def get_department(session: SessionDep) -> List[HRDepartment]:
    statement = select(HRDepartment)
    departments = session.exec(statement).all()
    return departments


DepartList = Annotated[HRDepartment, Depends(get_department)]


def get_tree(depart_list: DepartList) -> Dict[int, HRDepartment]:
    """
    Builds a hierarchical structure of departments from a list of department records.

    Args:
        depart_list (DepartList): List of department records

    Returns:
        tuple: A tuple containing the root departments and the hierarchical structure of all departments
    """

    departments = {}
    # root_departments = []
    for row in depart_list:
        # id, _code, dept_name, dept_parentcode = row
        departments[row.dept_code] = {
            "id": row.id,
            "dept_code": row.dept_code,
            "dept_name": row.dept_name,
            "dept_parentcode": row.dept_parentcode,
            "children": {},
            "descendants": [row.id],
            "level": 0
        }
        # if row.dept_parentcode == 0:
        #     root_departments.append(departments[row.dept_code])
    for dept_code, dept in departments.items():
        parent_code = dept["dept_parentcode"]
        if parent_code != 0:
            departments[parent_code]["children"][dept_code] = dept

    def _set_level(department, current_level):
        # dept_data = departments[department]
        department["level"] = current_level
        for _code, child_dept in department["children"].items():
            _set_level(child_dept, current_level + 1)

    def _set_descendantss(dept_part, list_id):
        for _code, _chd in departments.items():
            if _chd["dept_parentcode"] == dept_part["dept_code"]:
                list_id.append(_chd["id"])
                _set_descendantss(_chd, list_id)

    for _code, dept in departments.items():
        _set_descendantss(dept, dept["descendants"])
        if dept["dept_parentcode"] == 0:
            _set_level(dept, 0)
    # return root_departments, departments
    return departments


def get_current_user(session: SessionDep, token: TokenDep) -> User:
    """
    Get current user from a given token.

    Args:
    - session (SessionDep): Database session.
    - token (TokenDep): Bearer token.

    Raises:
    - HTTPException: If the token is invalid or the user does not exist or is inactive.

    Returns:
    - User: The current user.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(User, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def get_current_active_superuser(current_user: CurrentUser) -> User:
    """
    Check if the current user is active and a superuser.

    If the current user is not a superuser, raises HTTPException(403).

    Returns the current user.
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
