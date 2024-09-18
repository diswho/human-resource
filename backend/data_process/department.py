import psycopg2

# Database connection details
host = "localhost"
database = "app"
user = "postgres"
password = "I536ib9E6HVxgc"

def build_department_hierarchy():

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=host, database=database, user=user, password=password
    )

    # Create a cursor object
    curs = conn.cursor()

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
    curs.execute(query)

    # Fetch all rows
    rows = curs.fetchall()

    # Create a dictionary to store departments and their hierarchy
    departments = {}
    root_departments = []
    check_list = []
    new_list = []
    # Iterate through the rows and build the hierarchy
    for row in rows:
        id, _code, dept_name, dept_parentcode = row
        departments[_code] = {
            "id": id,
            "dept_code": _code,
            "dept_name": dept_name,
            "dept_parentcode": dept_parentcode,
            "children": {},
            "children_id": [id],
            "level": 0  # Initialize level to 0
        }
        if dept_parentcode == '0':
            root_departments.append(departments[_code])

    # Add children to each department
    for dept_code, dept in departments.items():
            parent_code = dept["dept_parentcode"]
            if parent_code != '0':
                departments[parent_code]["children"][dept_code] = dept


    # Set department levels recursively
    def _set_level(department, current_level):
        # dept_data = departments[department]
        department["level"] = current_level
        for _id,child_dept in department["children"].items():
            _set_level(child_dept, current_level + 1)


    # Set children_ids Departments
    def _set_children_ids(dept_part, list_id):
        for _code, _chd in departments.items():
            if _chd["dept_parentcode"] == dept_part["dept_code"]:
                list_id.append(_chd["id"])
                _set_children_ids(_chd, list_id)


    for codes, dept in departments.items():
        _set_children_ids(dept, dept["children_id"])
        if dept["dept_parentcode"] == '0':
            _set_level(dept, 0)

    # Close the cursor and connection
    curs.close()
    conn.close()
    return root_departments, departments

# Example usage:
root_departments, departments = build_department_hierarchy()

# Access the hierarchical data:
for root_dept in root_departments:
    print(f"Department: {root_dept['dept_name']}")
    print(f"  Children: {root_dept['children_id']}")