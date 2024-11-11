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
import { z } from "zod"
// import useAuth from "../../hooks/useAuth";
import { DepartmentService, EmployeesService } from "../../client";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useEffect, useState } from "react";

const employeesSearchSchema = z.object({
  page: z.number().catch(1),
})

export const Route = createFileRoute("/_layout/employee")({
  component: Employee,
  validateSearch: (search) => employeesSearchSchema.parse(search),
});

const PER_PAGE = 15
function getEmployeeService({ page }: { page: number }) {
  return {
    queryFn: () => EmployeesService.readEmployees({ skip: (page - 1) * PER_PAGE, limit: PER_PAGE }),
    queryKey: ["employees", { page }]
  }
}
function getDepartmentService() {
  return {
    queryFn: () => DepartmentService.getDepartment(),
    queryKey: ["departments", {}]
  }
}
function CascadingDropdown() {
  // cascading dropdown menu for departments
  
}
function EmployeeTable() {
  const queryClient = useQueryClient()
  const { page } = Route.useSearch()
  const navigate = useNavigate({ from: Route.fullPath })
  const setPage = (page: number) => navigate({ search: (prev) => ({ ...prev, page }) })
  const { data: employees, isPending, isPlaceholderData } = useQuery({
    ...getEmployeeService({ page }),
    placeholderData: (prevData) => prevData,
  })
  const hasNextPage = !isPlaceholderData && employees?.data.length === PER_PAGE
  const hasPreviousPage = page > 1

  useEffect(() => {
    if (hasNextPage) {
      queryClient.prefetchQuery(getEmployeeService({ page: page + 1 }))
    }
  }, [page, queryClient, hasNextPage])

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
          {isPending ? (<Tbody>
            <Tr>
              {new Array(9).fill(null).map((_, index) => (
                <Td key={index}>
                  <SkeletonText noOfLines={1} paddingBlock="16px" />
                </Td>
              ))}
            </Tr>
          </Tbody>) : (
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

      <Flex gap={4}
        alignItems="center"
        mt={4}
        direction="row"
        justifyContent="flex-start">
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


function Employee() {
  // const { user: currentUser } = useAuth();

  return (
    <>
      <Container maxW="full">
        <Heading size="lg" textAlign={{ base: "center", md: "left" }} py={12}>
          Employee Dashboard
        </Heading>
        <CascadingDropdown />
        <EmployeeTable />
      </Container>
    </>
  );
}
