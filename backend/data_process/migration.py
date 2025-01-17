import sqlite3
import psycopg2

# SQLite database details
sqlite_db_path = 'C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db'
# sqlite_db_path = '/home/phuong/Documents/Database/Xothavy/ZKTimeNet.db'

# psycopg2-binary

# PostgreSQL database details
postgres_host = 'localhost'
postgres_database = 'app'
postgres_user = 'postgres'
postgres_password = 'I536ib9E6HVxgc'


# List of tables to migrate
# tables_to_migrate = ['att_DayType', 'att_day_summary', 'att_employee_shift', 'att_punches', 'att_shift_details', 'att_shift',
#                      'att_StatisticItem', 'att_timetable', 'hr_company', 'hr_department', 'hr_employee', 'hr_position']  # Replace with actual table names
tables_to_migrate = ['att_DayType']

# Connect to SQLite database
sqlite_conn = sqlite3.connect(sqlite_db_path)
sqlite_cursor = sqlite_conn.cursor()

# Connect to PostgreSQL database
postgres_conn = psycopg2.connect(
    host=postgres_host,
    database=postgres_database,
    user=postgres_user,
    password=postgres_password
)
postgres_cursor = postgres_conn.cursor()

# Loop through each table and migrate data
for table_name in tables_to_migrate:
    # Get table schema from SQLite database
    sqlite_cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
    columns = [desc[0] for desc in sqlite_cursor.description]

    # Create table in PostgreSQL database
    postgres_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {', '.join(f'{column} VARCHAR(255)' for column in columns)}
        );
    """)

    # Get data from SQLite database
    sqlite_cursor.execute(f"SELECT * FROM {table_name}")
    data = sqlite_cursor.fetchall()

    # Insert data into PostgreSQL database
    for row in data:
        insert_values = ', '.join(['%s'] * len(row))
        postgres_cursor.execute(f"INSERT INTO {table_name} VALUES ({insert_values})", row)
        # Print the executed query
        print(postgres_cursor.query)

    # Commit changes and close connections
    print(f"Migrated table '{table_name}'")

postgres_conn.commit()
postgres_conn.close()
sqlite_conn.close()

print("Migration complete!")
# python backend\data_process\migration.py
