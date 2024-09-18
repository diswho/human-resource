import psycopg2


class Node:
    """Represents a node in a tree structure."""

    def __init__(self, id, dept_code, dept_name, dept_parentcode):
        self.id = id
        self.dept_code = dept_code
        self.dept_name = dept_name
        self.dept_parentcode = dept_parentcode
        self.children = []
        self.children_id = {id}

    def add_child(self, child):
        """Adds a child node to this node."""
        self.children.append(child)


def department_process(cursor):
    cursor.execute("SELECT id, dept_code, dept_name, dept_parentcode FROM hr_department")
    departments = cursor.fetchall()

    roots = []
    nodes = {}

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
            roots.append(dept_code)
        if dept_parentcode:
            parent_node = nodes[dept_parentcode]
            parent_node.add_child(nodes[dept_code])
    return nodes, roots


connect = psycopg2.connect(
    host="localhost",
    database="app",
    user="postgres",
    password="I536ib9E6HVxgc"
)

cursor = connect.cursor()
nodes, root = department_process(cursor)


def tree(node, level=0):
    """Prints the tree structure recursively."""
    print("  " * level + f"ID: {node.id}, Code: {node.dept_code}, Name: {node.dept_name}")
    for child in node.children:
        tree(child, level + 1)


def get_ids(node):
    ids = []

    def dfs(node):
        ids.append(node.id)
        for child in node.children:
            dfs(child)

    dfs(node)
    return ids


for code in root:
    tree(nodes[code])

ids = get_ids(nodes['1'])
print(ids)
cursor.close()
connect.close()
