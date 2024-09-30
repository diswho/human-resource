import sqlite3
import psycopg2

# SQLite database connection details
sqlite_db_path = 'C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db'
# sqlite_db_path = '/home/phuong/Documents/Database/Xothavy/ZKTimeNet.db'
sqlite_conn = sqlite3.connect(sqlite_db_path)

# PostgreSQL database connection details
postgres_host = 'localhost'
postgres_database = 'app'
postgres_user = 'postgres'
postgres_password = 'I536ib9E6HVxgc'

postgres_conn = psycopg2.connect(
    host=postgres_host,
    database=postgres_database,
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

# Function to update the PostgreSQL database with new records


def update_db(table_name):
    """
    Updates the PostgreSQL database with new records from the SQLite database.

    Args:
        table_name: The name of the table to update.
    """
    new_records = get_new_records(table_name)
    if new_records:
        with postgres_conn:
            cursor = postgres_conn.cursor()
            # Get the column names from the SQLite table
            # sql = f"PRAGMA table_info({table_name})"
            sql = "PRAGMA table_info(hr_employee)"
            cursor.execute(sql)
            column_names = [row[1] for row in cursor.fetchall()]

            for record in new_records:
                # Create a parameterized insert statement based on column names
                insert_query = f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({','.join(['%s'] * len(column_names))})"
                cursor.execute(insert_query, record)
            postgres_conn.commit()
            print(f"{len(new_records)} new records inserted into '{table_name}' table.")


# Example usage
update_db('hr_employee')  # Update the 'hr_employee' table
update_db('hr_department')  # Update the 'hr_department' table

# Close connections
sqlite_conn.close()
postgres_conn.close()
