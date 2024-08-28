import psycopg2


class Node:
    """Represents a node in a tree structure."""

    def __init__(self, id, dept_code, dept_name, dept_parentcode):
        self.id = id
        self.dept_code = dept_code
        self.dept_name = dept_name
        self.dept_parentcode = dept_parentcode
        self.children = []

    def add_child(self, child):
        """Adds a child node to this node."""
        self.children.append(child)


def department_process(cursor):
    cursor.execute("SELECT id, dept_code, dept_name, dept_parentcode FROM hr_department")
    departments = cursor.fetchall()

    department_list = {}
    nodes = {}
    root_dept = Node(0, '0', "xokthavy")

    # Build the tree structure
    for id, dept_code, dept_name, dept_parentcode in departments:
        node = Node(id, dept_code, dept_name, dept_parentcode)
        nodes[id] = node  # Store the node in the dictionary

    # Link parent-child relationships
    for id, dept_code, dept_name, dept_parentcode in departments:
        if dept_parentcode:
            parent_node = nodes[dept_parentcode]
            parent_node.add_child(nodes[id])

    return None


connect = psycopg2.connect(
    host="localhost",
    database="app",
    user="postgres",
    password="I536ib9E6HVxgc"
)

cursor = connect.cursor()
department_process = department_process(cursor)

print(department_process)
cursor.close()
connect.close()
