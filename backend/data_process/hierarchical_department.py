from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel, create_engine, Session

# Define the Department model using SQLModel
class Department(SQLModel, table=True):
    id: str = Field(primary_key=True)
    dept_code: str = Field(nullable=False)
    dept_name: str = Field(nullable=False)
    dept_parentcode: Optional[str] = Field(default=None)
    usecode: Optional[str] = Field(default=None)
    dept_operationmode: Optional[str] = Field(default=None)
    middleware_id: Optional[str] = Field(default=None)
    defaultdepartment: Optional[str] = Field(default=None)
    company_id: Optional[str] = Field(default=None)
    linetoken: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

    # Define relationship to itself for building hierarchy
    children: List["Department"] = Relationship(back_populates="parent")
    parent: Optional["Department"] = Relationship(back_populates="children")

# Database connection settings
DATABASE_URL = "postgresql://postgres:I536ib9E6HVxgc@localhost:5432/app"
engine = create_engine(DATABASE_URL)

# Create tables if they don't exist
SQLModel.metadata.create_all(engine)

# Function to retrieve departments from the database
def get_departments():
    """Retrieves all departments from the database."""
    with Session(engine) as session:
        departments = session.exec(select(Department)).all()
        return departments

# Function to build the hierarchical structure
def build_hierarchy(departments: List[Department]):
    """Builds the hierarchical structure from the list of departments."""

    hierarchy = {}
    for dept in departments:
        hierarchy[dept.id] = {
            "dept_code": dept.dept_code,
            "dept_name": dept.dept_name,
            "parent_id": dept.dept_parentcode,  # Store the parent ID
            "children": [],
        }

    # Create the hierarchy iteratively
    root_departments = []
    for dept_id, dept_data in hierarchy.items():
        parent_id = dept_data["parent_id"]
        if parent_id is None:  # Root department has no parent
            root_departments.append(dept_id)
        else:
            hierarchy[parent_id]["children"].append(dept_id)

    return hierarchy, root_departments  # Return the hierarchy and root departments

# Get the departments from the database
departments = get_departments()

# Build the hierarchical structure
hierarchy, root_departments = build_hierarchy(departments)

# Function to retrieve a hierarchical department structure
def get_hierarchical_department(department_id: str, hierarchy):
    """Returns a hierarchical representation of a department."""

    department = hierarchy.get(department_id)
    if not department:
        return None

    # Recursively build the hierarchy
    children = []
    for child_id in department["children"]:
        children.append(get_hierarchical_department(child_id, hierarchy))

    return {
        "id": department_id,
        "dept_code": department["dept_code"],
        "dept_name": department["dept_name"],
        "children": children,
    }

# Get the hierarchical department structure for a given department ID
department_id = "your_department_id"
hierarchical_department = get_hierarchical_department(department_id, hierarchy)

# Print the hierarchical department structure
print(hierarchical_department)
