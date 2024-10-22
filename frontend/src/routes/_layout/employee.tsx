import { Box, Container, Text } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

import useAuth from "../../hooks/useAuth";
import { DepartmentService } from "../../client";

export const Route = createFileRoute("/_layout/employee")({
  component: Employee,
});

// create function component to get DepartmentService
function getDepartmentService() {
  return {queryFn:() => DepartmentService.getDepartment()};
}

function Employee() {
  const { user: currentUser } = useAuth();

  return (
    <>
      <Container maxW="full">
        <Box pt={12} m={4}>
          <Text>This is employee dashboard!{currentUser?.email}</Text>
        </Box>
      </Container>
    </>
  );
}
