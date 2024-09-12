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
        root_list.append(dept_code)

    departments[dept_code] = {
        "id": id,
        "dept_code": dept_code,
        "dept_name": dept_name,
        "dept_parentcode": dept_parentcode,
        "children": {},
        "level": 0  # Initial level set to 0
    }


def get_sub_dept(dept_code, list_id):
    for did, dept in departments.items():
        if dept["dept_parentcode"] == dept_code:
            dept_id = dept["id"]
            # if dept_id not in list_id:
            list_id.append(dept_id)
            get_sub_dept(dept["dept_code"], list_id)


for root_code in root_list:
    # departments[root_code]["id"]
    list_id = [departments[root_code]["id"]]
    get_sub_dept(root_code, list_id)
    print(list_id)

cursor.close()
connect.close()
