import psycopg2

# Database connection details
host = "localhost"
database = "app"
user = "postgres"
password = "I536ib9E6HVxgc"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host, database=database, user=user, password=password
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
root_departments = []
check_list = []
new_list = []
# Iterate through the rows and build the hierarchy
for row in rows:
    id, dept_code, dept_name, dept_parentcode = row
    departments[dept_code] = {
        "id": id,
        "dept_code": dept_code,
        "dept_name": dept_name,
        "dept_parentcode": dept_parentcode,
        "children": [],
        "children_id": [id],
        "level": 0  # Initialize level to 0
    }
    if dept_parentcode == '0':
        root_departments.append(departments[dept_code])

for dept in root_departments:
    check_list.append(dept["dept_code"])

for chck in check_list:
    for cid, child_node in departments.items():
        if child_node["dept_parentcode"] == chck:

# for pid, parent_node in departments.items():
#     for cid, child_node in departments.items():
#         if child_node["dept_parentcode"] == parent_node["dept_code"]:
#             child_node["level"] + 1
#             for lst_id in child_node["children_id"]:
#                 if lst_id not in parent_node["children_id"]:
#                     parent_node["children_id"].append(child_node["id"])

# current list id =>root_departments
# new list id
# set current to new

# for code, data in departments.items():
#     check_code = data
#     while check_code["dept_parentcode"] != '0':
#         parentcode = check_code["dept_parentcode"]
#         if check_code["id"] not in departments[parentcode]["children_id"]:
#             departments[parentcode]["children"].append(check_code)
#             departments[parentcode]["children_id"].append(check_code["id"])
#         check_code = departments[parentcode]


# Close the cursor and connection
cur.close()
conn.close()
