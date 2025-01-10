#! /usr/bin/env bash

# Let the DB start
python /app/app/backend_pre_start.py
# python app/backend_pre_start.py

# Run migrations

# ```console
# $ alembic revision --autogenerate -m "description_of_changes"
# alembic revision -m "Update s column types"
# ```
# After creating the revision, run the migration in the database (this is what will actually change the database):
# alembic upgrade head
# alembic downgrade 4960ae64aad1

# Create initial data in DB
python /app/app/initial_data.py
# python app/initial_data.py
