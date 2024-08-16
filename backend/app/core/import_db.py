import sqlite3
import psycopg2

# SQLite database connection details
sqlite_db_path = '/home/phuong/Documents/Database/Xothavy/ZKTimeNet.db'
sqlite_conn = sqlite3.connect(sqlite_db_path)

# PostgreSQL database connection details
postgres_host = 'your_postgres_host'  # Replace with your host
postgres_db = 'your_postgres_db'    # Replace with your database name
postgres_user = 'your_postgres_user' # Replace with your user
postgres_password = 'your_postgres_password' # Replace with your password
postgres_conn = psycopg2.connect(
    host=postgres_host,
    database=postgres_db,
    user=postgres_user,
    password=postgres_password
)

# Function to fetch new records from SQLite
def get_new_records(table_name):
    """
    Fetches new records from a SQLite table based on the last inserted ID in PostgreSQL.
    """
    with sqlite_conn:
        cursor = sqlite_conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        sqlite_records = cursor.fetchall()

    with postgres_conn:
        cursor = postgres_conn.cursor()
        cursor.execute(f"SELECT MAX(id) FROM {table_name}")
        last_postgres_id = cursor.fetchone()[0]

    new_records = []
    if last_postgres_id is None:
        # No records in PostgreSQL yet, import all from SQLite
        return sqlite_records
    else:
        for record in sqlite_records:
            if record[0] > last_postgres_id:  # Assuming ID is the first column
                new_records.append(record)
    return new_records

# Example usage for table 'employees'
new_employees = get_new_records('employees')
if new_employees:
    with postgres_conn:
        cursor = postgres_conn.cursor()
        for employee in new_employees:
            # Assuming column names match between databases
            cursor.execute(f"""
                INSERT INTO employees (id, name, department) 
                VALUES (%s, %s, %s)
            """, (employee[0], employee[1], employee[2]))
        postgres_conn.commit()
        print(f"{len(new_employees)} new records inserted into 'employees' table.")

# Close connections
sqlite_conn.close()
postgres_conn.close()
