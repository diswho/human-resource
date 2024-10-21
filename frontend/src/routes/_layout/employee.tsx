import { Box, Container, Text } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

import useAuth from "../../hooks/useAuth";

export const Route = createFileRoute("/_layout/employee")({
  component: Employee,
});

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
