import psycopg2

# Database connection details
postgres_host = 'localhost'
postgres_database = 'app'
postgres_user = 'postgres'
postgres_password = 'I536ib9E6HVxgc'

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=postgres_host, database=postgres_database, user=postgres_user, password=postgres_password
)

# Create a cursor object
cur = conn.cursor()

# SQL query to retrieve department data
query = """
SELECT
    id,
    dept_code,
    dept_name,
    dept_parentcode
FROM
    public.hr_department;
"""

# Execute the query
cur.execute(query)

# Fetch all rows
rows = cur.fetchall()

# Create a dictionary to store departments and their hierarchy
departments = {}

# Iterate through the rows and build the hierarchy
for row in rows:
    id, dept_code, dept_name, dept_parentcode = row
    departments[dept_code] = {
        "id": id,
        "dept_name": dept_name,
        "parent_id": dept_parentcode,
        "children": []  # Initialize an empty list for children
    }

# Build the hierarchical structure iteratively
def build_hierarchy(departments):
    """Builds the hierarchical structure from the departments dictionary."""

    root_departments = []
    for dept_id, dept_data in departments.items():
        parent_id = dept_data["parent_id"]
        if parent_id == '0':  # Check for root departments
            root_departments.append(dept_id)
        else:
            departments[parent_id]["children"].append(dept_id)

    return root_departments

# Get the root departments (those with no parent)
root_departments = build_hierarchy(departments)

# Function to get hierarchical department structure
def get_hierarchical_department(department_id, departments):
    """Returns a hierarchical representation of a department."""

    department = departments.get(department_id)
    if not department:
        return None

    # Recursively build the hierarchy
    children = []
    for child_id in department["children"]:
        children.append(get_hierarchical_department(child_id, departments))

    # Return the department data with its children
    return {
        "id": department_id,
        "dept_code": department["dept_code"],
        "dept_name": department["dept_name"],
        "children": children,
    }

# Get the hierarchical department structure for a given department ID
department_id = "19"
hierarchical_department = get_hierarchical_department(department_id, departments)

# Print the hierarchical department structure
print(hierarchical_department)

# Close the cursor and connection
cur.close()
conn.close()