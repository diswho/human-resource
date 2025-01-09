#! /usr/bin/env bash

# Let the DB start
python /app/app/backend_pre_start.py
python app/backend_pre_start.py

# Run migrations

# ```console
# $ alembic revision --autogenerate -m "hr_performance"
# ```
# After creating the revision, run the migration in the database (this is what will actually change the database):
alembic upgrade head

# Create initial data in DB
python /app/app/initial_data.py
python app/initial_data.py
