import {
  Container,
  Heading,
  SkeletonText,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
  useQuery,
} from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

// import useAuth from "../../hooks/useAuth";
import { DepartmentService } from "../../client";

export const Route = createFileRoute("/_layout/employee")({
  component: Employee,
});

// create function component to get DepartmentService
function getDepartmentService() {
  return { queryFn: () => DepartmentService.getDepartment() };
}
function EmployeeTable() {
  // Mock data for demonstration purposes
  // const employees = [
  //   { id: 1, name: "John Doe", position: "Developer", department: "IT" },
  //   { id: 2, name: "Jane Smith", position: "Designer", department: "Creative" },
  //   { id: 3, name: "Mike Johnson", position: "Manager", department: "HR" },
  // ];

  return (
    <TableContainer>
      <Table size={{ base: "sm", md: "md" }}>
        <Thead>
          <Tr>
            <Th>Name</Th>
            <Th>Position</Th>
            <Th>Department</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            {new Array(3).fill(null).map((_, index) => (
              <Td key={index}>
                <SkeletonText noOfLines={1} paddingBlock="16px" />
              </Td>
            ))}
          </Tr>
        </Tbody>
      </Table>
    </TableContainer>
  );
}

function Employee() {
  // const { user: currentUser } = useAuth();

  return (
    <>
      <Container maxW="full">
        <Heading size="lg" textAlign={{ base: "center", md: "left" }} py={12}>
          Employee Dashboard
        </Heading>
        <EmployeeTable />
      </Container>
    </>
  );
}
