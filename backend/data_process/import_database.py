import logging
# import sqlite3
from sqlalchemy import func
from sqlmodel import Session, create_engine, select
from app.core.config import settings
from app import crud
from app.models.hr_department import HRDepartment
import json

from app.models.hr_employee import HREmployee

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SQLite database connection details
# sqlite_db_path = '/home/phuong/Documents/Database/Xothavy/ZKTimeNet.db'
sqlite_db_path = "C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"
engine_sqlite = create_engine(f"sqlite:///{sqlite_db_path}")

# PostgreSQL database connection details
engine_postgres = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
# Function to fetch new records from SQLite


def init() -> None:
    with Session(engine_sqlite) as session_sqlite, Session(engine_postgres) as session_postgres:
        dept_sqlite_records = session_sqlite.exec(select(HRDepartment)).all()
        employee_sqlite_records = session_sqlite.exec(select(HREmployee)).all()
        dept_last_postgres_id = session_postgres.exec(select(func.max(HRDepartment.id))).first()
        employee_last_postgres_id = session_postgres.exec(select(func.max(HREmployee.id))).first()

    new_records = []

    if dept_last_postgres_id is None:
        new_records = dept_sqlite_records
    else:
        new_records = [record for record in dept_sqlite_records if record.id > dept_last_postgres_id]

    if new_records:
        for record in new_records:
            record_dict = record.model_dump()
            crud.create_department(session=session_postgres, department_in=record_dict)


def main() -> None:
    logger.info("Creating import data")
    init()
    logger.info("import data finish")


if __name__ == "__main__":
    main()
