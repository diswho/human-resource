import json
import psycopg2


def build_department_tree(conn, cursor):
    """
    Builds a department tree from a PostgreSQL database, including department levels.

    Args:
      conn: A psycopg2 connection to the database.
      cursor: A psycopg2 cursor for executing SQL queries.

    Returns:
      A dictionary representing the department tree, where keys are department codes
      and values are dictionaries with the following structure:
        {
          "name": department name,
          "parent_code": parent department code (None if top-level),
          "children": {},  # Dictionary for child departments
          "level": department level in the hierarchy (0 for root)
        }
    """

    # Get all departments from the database
    cursor.execute("SELECT id, dept_code, dept_name, dept_parentcode FROM hr_department")
    departments = cursor.fetchall()

    # Create a dictionary to store the department tree
    department_tree = {}
    respond_tree = {}

    # Iterate over departments and build the tree structure
    for id, dept_code, dept_name, dept_parentcode in departments:
        # Replace '0' with None for top-level departments
        if dept_parentcode == '0':
            dept_parentcode = None

        department_tree[dept_code] = {
            "id": id,
            "name": dept_name,
            "parent_code": dept_parentcode,
            "children": {},
            "level": 0  # Initial level set to 0
        }

    # Calculate levels recursively
    def calculate_level(dept_code, current_level):
        dept_data = department_tree[dept_code]
        dept_data["level"] = current_level
        for child_code in dept_data["children"]:
            calculate_level(child_code, current_level + 1)

    # Add children to each department
    for dept_code, dept_data in department_tree.items():
        parent_code = dept_data["parent_code"]
        if parent_code == '0':
            parent_code = None
        if parent_code is not None:
            department_tree[parent_code]["children"][dept_code] = department_tree[dept_code]

    # Calculate levels for all departments starting from root
    for dept_code, dept_data in department_tree.items():
        if dept_data["parent_code"] is None:  # Root department
            calculate_level(dept_code, 0)

    for dept_code, dept_data in department_tree.items():
        if dept_data['parent_code'] is None:
            respond_tree[dept_code] = dept_data

    json_tree = json.dumps(respond_tree, indent=4, ensure_ascii=False)
    # Return the department tree
    return json_tree


# Example usage (same as before):
# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="app",
    user="postgres",
    password="I536ib9E6HVxgc"
)

# Create a cursor
cursor = conn.cursor()

# Build the department tree
department_tree = build_department_tree(conn, cursor)

# Print the department tree (for example)
print(department_tree)

# Close the cursor and connection
cursor.close()
conn.close()


# postgres_host = 'localhost'
# postgres_database = 'app'
# postgres_user = 'postgres'
# postgres_password = 'I536ib9E6HVxgc'
