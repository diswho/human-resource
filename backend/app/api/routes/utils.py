from typing import Any, Dict, List, Tuple
from app.models.hr_department import HRDepartment, HRDepartmentPublic
from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from app.api.deps import DepartList, get_current_active_superuser, get_tree
from app.models.models import Message
from app.utils import generate_test_email, send_email

router = APIRouter()


@router.post("/test-email/", dependencies=[Depends(get_current_active_superuser)],    status_code=201,)
def test_email(email_to: EmailStr) -> Message:
    """
    Test emails.
    """
    email_data = generate_test_email(email_to=email_to)
    send_email(
        email_to=email_to,
        subject=email_data.subject,
        html_content=email_data.html_content,
    )
    return Message(message="Test email sent")


@router.get("/get-department/", response_model=Dict[int, HRDepartmentPublic], status_code=201)
def get_department(departList: DepartList) -> Dict[int, HRDepartmentPublic]:
    """
    Get departments.

    Returns:
    List[HRDepartmentPublic]: List of department records
    """
    roots = []
    departs = []
    try:
        departs = get_tree(departList)
        # roots, departs = get_trees
    except AttributeError as e:
        if "NoneType" in str(e):
            raise AttributeError("One of the objects in the list is None")
        else:
            raise
    except Exception as e:
        raise
    return departs
