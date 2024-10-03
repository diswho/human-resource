from array import ArrayType
import logging
# import sqlite3
from sqlalchemy import func
from sqlmodel import SQLModel, Session, create_engine, select
from app.core.config import settings
from app import crud
from app.models.att_StatisticItem import AttStatisticItem
from app.models.att_day_summary import AttDaySummary
from app.models.att_DayType import AttDayType
from app.models.att_employee_shift import AttEmployeeShift
from app.models.att_punches import AttPunches
from app.models.att_shift import AttShift
from app.models.att_timetable import AttTimetable
from app.models.hr_department import HRDepartment
from datetime import datetime

from app.models.hr_employee import HREmployee
from app.models.hr_position import HRPosition

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SQLite database connection details
# sqlite_db_path = '/home/phuong/Documents/Database/Xothavy/ZKTimeNet.db'
sqlite_db_path = "C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"
engine_sqlite = create_engine(f"sqlite:///{sqlite_db_path}")

# PostgreSQL database connection details
engine_postgres = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
# Function to fetch new records from SQLite


def init_model(model: SQLModel) -> None:
    with Session(engine_sqlite) as session_sqlite, Session(engine_postgres) as session_postgres:
        date_string = '2023-05-01 00:00:00.000'
        date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')

        statement = select(model)
        if model == AttPunches:
            statement = select(model).where(model.punch_time > date_object)
        elif model == AttDaySummary:
            statement = select(model).where(model.att_date > date_object)

        sqlite_records = session_sqlite.exec(statement).all()
        last_postgres_id = session_postgres.exec(select(func.max(model.id))).first()
        print(last_postgres_id)

    new_records = []
    if last_postgres_id is None:
        new_records = sqlite_records
    else:
        new_records = [record for record in sqlite_records if record.id > last_postgres_id]

    if new_records:
        for record in new_records:
            record_dict = record.model_dump()
            obj = model.model_validate(record_dict)
            session_postgres.add(obj)
            session_postgres.commit()
            session_postgres.refresh(obj)


def main() -> None:
    logger.info("Creating import data")
    # init_model(HRDepartment)
    # init_model(HRPosition)
    # init_model(HREmployee)
    # init_model(AttStatisticItem)
    # init_model(AttTimetable)
    # init_model(AttShift)
    # init_model(AttPunches)
    # init_model(AttEmployeeShift)
    # init_model(AttDayType)
    init_model(AttDaySummary)
    logger.info("import data finish")


if __name__ == "__main__":
    main()
