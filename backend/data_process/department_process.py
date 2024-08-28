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

    department_list = []
    nodes = {}
    # root_dept = Node(0, '0', "xokthavy")

    # Build the tree structure
    for id, dept_code, dept_name, dept_parentcode in departments:
        if dept_parentcode == '0':
            dept_parentcode = None
        node = Node(id, dept_code, dept_name, dept_parentcode)
        nodes[dept_code] = node  # Store the node in the dictionary

    # Link parent-child relationships
    for id, dept_code, dept_name, dept_parentcode in departments:
        if dept_parentcode == '0':
            dept_parentcode = None
            department_list.append(dept_code)
        if dept_parentcode:
            parent_node = nodes[dept_parentcode]
            parent_node.add_child(nodes[dept_code])

    def print_tree(node, level=0):
        """Prints the tree structure recursively."""
        print("  " * level + f"ID: {node.id}, Code: {node.dept_code}, Name: {node.dept_name}")
        for child in node.children:
            print_tree(child, level + 1)

    # root = nodes[departments[0][0]]
    # print_tree(root)
    for id in department_list:
        print_tree(nodes[id])
    
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
