import psycopg2

connect = psycopg2.connect(
    host="localhost",
    database="app",
    user="postgres",
    password="I536ib9E6HVxgc"
)

cursor = connect.cursor()
# Get all departments from the database
cursor.execute("SELECT id, dept_code, dept_name, dept_parentcode FROM hr_department")
result = cursor.fetchall()
root_list = []

departments = {}


# Iterate over departments and build the tree structure
for id, dept_code, dept_name, dept_parentcode in result:
    # Replace '0' with None for top-level departments
    if dept_parentcode == '0':
        dept_parentcode = None
        # root_list.append(dept_code)

    departments[dept_code] = {
        "id": id,
        "dept_code": dept_code,
        "dept_name": dept_name,
        "dept_parentcode": dept_parentcode,
        "children": {},
        "list_id": [id],
        "level": 0  # Initial level set to 0
    }
    if dept_parentcode == None:
        root_list.append(departments[dept_code])

# Add children to each department
for dept_code, dept_data in departments.items():
    parent_code = dept_data["dept_parentcode"]
    if parent_code == '0':
        parent_code = None
    if parent_code is not None:
        departments[parent_code]["children"][dept_code] = departments[dept_code]


def calculate_level(dept_code, current_level):  # Calculate levels recursively
    dept_data = departments[dept_code]
    dept_data["level"] = current_level
    for child_code in dept_data["children"]:
        calculate_level(child_code, current_level + 1)


for root_node in root_list:
    calculate_level(root_node, 0)


def get_sub_dept(dept_part, list_id):
    for codes, dept_chd in departments.items():
        if dept_chd["dept_parentcode"] == dept_part["dept_code"]:
            list_id.append(dept_chd["id"])
            get_sub_dept(dept_chd, list_id)


for codes, dept in departments.items():
    get_sub_dept(dept, dept["list_id"])

cursor.close()
connect.close()
