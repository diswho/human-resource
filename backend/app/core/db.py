from sqlmodel import Session, create_engine, select

from app import crud
from app.core.config import settings
from app.models.user import User, UserCreate
from app.models.hr_department import HRDepartment
from app.models.hr_company import HRCompany

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/fastapi/full-stack-fastapi-template/issues/28


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    from sqlmodel import SQLModel

    # from app.core.engine import engine
    # This works because the models are already imported and registered from app.models
    SQLModel.metadata.create_all(engine)

    company_name = "Xokthavy trade import-export sole Co.,Ltd"
    company = session.exec(select(HRCompany).where(HRCompany.cmp_name == company_name)).first()
    if not company:
        company_create = HRCompany(cmp_name=company_name)
        company = crud.create_company(session=session, company_create=company_create)

    user = session.exec(select(User).where(User.email == settings.FIRST_SUPERUSER)).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)
