import {
  Button,
  Container,
  Flex,
  Heading,
  SkeletonText,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react";
import { createFileRoute, useNavigate } from "@tanstack/react-router";
import { z } from "zod";
// import useAuth from "../../hooks/useAuth";
import {
  DepartmentService,
  EmployeesService,
  HRDepartmentPublic,
} from "../../client";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useEffect, useState } from "react";

const employeesSearchSchema = z.object({
  page: z.number().catch(1),
});

export const Route = createFileRoute("/_layout/employee")({
  component: Employee,
  validateSearch: (search) => employeesSearchSchema.parse(search),
});

const PER_PAGE = 15;
function getEmployeeService({ page }: { page: number }) {
  return {
    queryFn: () =>
      EmployeesService.readEmployees({
        skip: (page - 1) * PER_PAGE,
        limit: PER_PAGE,
      }),
    queryKey: ["employees", { page }],
  };
}

function EmployeeTable() {
  const queryClient = useQueryClient();

  const { page } = Route.useSearch();
  const navigate = useNavigate({ from: Route.fullPath });
  const setPage = (page: number) =>
    navigate({ search: (prev) => ({ ...prev, page }) });
  const {
    data: employees,
    isPending,
    isPlaceholderData,
  } = useQuery({
    ...getEmployeeService({ page }),
    placeholderData: (prevData) => prevData,
  });
  const hasNextPage = !isPlaceholderData && employees?.data.length === PER_PAGE;
  const hasPreviousPage = page > 1;

  useEffect(() => {
    if (hasNextPage) {
      queryClient.prefetchQuery(getEmployeeService({ page: page + 1 }));
    }
  }, [page, queryClient, hasNextPage]);

  return (
    <>
      <TableContainer>
        <Table size={{ base: "sm", md: "md" }}>
          <Thead>
            <Tr>
              <Th>emp_pin</Th>
              <Th>emp_ssn</Th>
              <Th>emp_firstname</Th>
              <Th>emp_lastname</Th>
              <Th>emp_phone</Th>
              <Th>emp_hiredate</Th>
              <Th>emp_title</Th>
              <Th>emp_birthday</Th>
            </Tr>
          </Thead>
          {isPending ? (
            <Tbody>
              <Tr>
                {new Array(9).fill(null).map((_, index) => (
                  <Td key={index}>
                    <SkeletonText noOfLines={1} paddingBlock="16px" />
                  </Td>
                ))}
              </Tr>
            </Tbody>
          ) : (
            <Tbody>
              {employees?.data.map((employee) => (
                <Tr key={employee.id}>
                  <Td>{employee.emp_pin}</Td>
                  <Td>{employee.emp_ssn}</Td>
                  <Td>{employee.emp_firstname}</Td>
                  <Td>{employee.emp_lastname}</Td>
                  <Td>{employee.emp_phone}</Td>
                  <Td>{employee.emp_hiredate}</Td>
                  <Td>{employee.emp_title}</Td>
                  <Td>{employee.emp_birthday}</Td>
                </Tr>
              ))}
            </Tbody>
          )}
        </Table>
      </TableContainer>

      <Flex
        gap={4}
        alignItems="center"
        mt={4}
        direction="row"
        justifyContent="flex-start"
      >
        <Button onClick={() => setPage(page - 1)} isDisabled={!hasPreviousPage}>
          Previous
        </Button>
        <Button isDisabled={!hasNextPage} onClick={() => setPage(page + 1)}>
          Next
        </Button>
      </Flex>
    </>
  );
}
interface Departments {
  [key: string]: HRDepartmentPublic;
}

function getDepartmentService() {
  return {
    queryFn: () => DepartmentService.getDepartment(),
    queryKey: ["departments", {}],
  };
}
function CascadingDropdown({ department }: { department: HRDepartmentPublic }) {
  // multi cascading dropdown menu for departments
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen((prev) => !prev);
  };

  return (
    <div style={{ marginLeft: `${department.level * 20}px`, padding: "5px 0" }}>
      <button
        onClick={toggleDropdown}
        style={{
          cursor: "pointer",
          background: "none",
          border: "none",
          textAlign: "left",
          fontWeight: "bold",
        }}
      >
        {department.dept_name} {department.children && (isOpen ? "▲" : "▼")}
      </button>
      {isOpen && department.children && (
        <div
          style={{
            marginTop: "5px",
            paddingLeft: "10px",
            borderLeft: "1px solid #ccc",
          }}
        >
          {Object.values(department.children).map((child) => (
            <CascadingDropdown key={child.dept_code} department={child} />
          ))}
        </div>
      )}
    </div>
  );
}
// function CascadingMenu({  departments = {}}: {  departments?: { [key: string]: HRDepartmentPublic };}) {
function CascadingMenu({ departments }: { departments: Departments }) {
  const rootDepartments = Object.values(departments).filter(
    (dept) => dept.dept_parentcode === 0
  );
  const [isOpen, setIsOpen] = useState(false);
  const toggleDropdown = () => {
    setIsOpen((prev) => !prev);
  };
  return (
    <>
      <div style={{ padding: "5px 0" }}>
        <button
          onClick={toggleDropdown}
          style={{
            cursor: "pointer",
            background: "none",
            border: "none",
            textAlign: "left",
            fontWeight: "bold",
          }}
        >
          Departent {isOpen ? "▲" : "▼"}
        </button>
        {isOpen && (
          <div>
            {rootDepartments.map((department) => (
              <CascadingDropdown
                key={department.dept_code}
                department={department}
              />
            ))}
          </div>
        )}
      </div>
    </>
  );
}

interface DepartmentProps {
  data: HRDepartmentPublic[];
}

const buildHierarchy = (departments: HRDepartmentPublic[], parentCode: number = 0): HRDepartmentPublic[] => {
  return departments
    .filter(department => department.dept_parentcode === parentCode)
    .map(department => ({
      ...department,
      children: buildHierarchy(departments, department.dept_code)
    }));
};

const renderMenu = (departments: HRDepartmentPublic[]) => {
  return (
    
    <ul>
      {departments.map(department => (
        <div style={{ marginLeft: `${department.level * 20}px`, padding: "5px 0" }}>
        <li key={department.id}>
          {department.dept_name}
          {department.children && department.children.length > 0 && renderMenu(department.children)}
        </li>
        </div>
      ))}
    </ul>
  );
};

const DepartmentMenu: React.FC<DepartmentProps> = ({ data }) => {
  const hierarchy = buildHierarchy(data);
  return <div>{renderMenu(hierarchy)}</div>;
};

function Employee() {
  // const queryClient = useQueryClient();

  const {
    data: departments,
    isLoading,
    isError,
    error,
    isFetching,
  } = useQuery({
    ...getDepartmentService(),
    placeholderData: { data: [] as HRDepartmentPublic[], count: 0 },
  });

  if (isLoading) {
    return <div>Loading departments...</div>;
  }

  if (isError) {
    return <div>Error loading departments: {error.message}</div>;
  }
  // Builds a hierarchical structure of departments from a list of departments
  // const departmentHierarchy = DepartmentMenu(departments?.data || []);
  // console.log(departmentHierarchy);

  const departmentShape = (departments?.data || []).reduce((acc, dept) => {
    acc[dept.dept_code] = dept;
    return acc;
  }, {} as Departments);


  return (
    <>
      <Container maxW="full">
        <Heading size="lg" textAlign={{ base: "center", md: "left" }} py={12}>
          Employee Dashboard
        </Heading>
        <DepartmentMenu data={departments?.data || []} />
        <CascadingMenu departments={departmentShape} />
        {isFetching && <div>Updating...</div>}
        <EmployeeTable />
      </Container>
    </>
  );
}
