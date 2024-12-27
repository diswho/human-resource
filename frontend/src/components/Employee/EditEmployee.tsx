import { useMutation, useQueryClient } from "@tanstack/react-query"
import { EmployeePublic } from "../../client/models"
import useCustomToast from "../../hooks/useCustomToast"
import { type SubmitHandler, useForm } from "react-hook-form"
import { ApiError, EmployeesService } from "../../client"
import { emailPattern, handleError } from "../../utils"
import { Button, FormControl, FormErrorMessage, FormLabel, Input, Modal, ModalBody, ModalCloseButton, ModalContent, ModalFooter, ModalHeader, ModalOverlay } from "@chakra-ui/react"

interface EditEmployeeProps {
    employee: EmployeePublic
    isOpen: boolean
    onClose: () => void
}

interface EmployeeUpdateForm extends EmployeePublic {
    // confirm_password: string

}

const EditEmployee = ({ employee, isOpen, onClose }: EditEmployeeProps) => {
    const queryClient = useQueryClient()
    const showToast = useCustomToast()

    const {
        register,
        handleSubmit,
        reset,
        formState: { errors, isSubmitting, isDirty },
    } = useForm<EmployeeUpdateForm>({
        mode: "onBlur",
        criteriaMode: "all",
        defaultValues: employee,
    })

    const mutation = useMutation({
        mutationFn: (data: EmployeePublic) => EmployeesService.updateEmployee({ id: employee.id, requestBody: data }),
        onSuccess: () => {
            showToast("Success!", "User updated successfully.", "success")
            onClose()
        },
        onError: (err: ApiError) => {
            handleError(err, showToast)
        },
        onSettled: () => {
            queryClient.invalidateQueries({ queryKey: ["users"] })
        },
    })

    const onSubmit: SubmitHandler<EmployeeUpdateForm> = async (data) => {
        // if (data.password === "") {
        //     data.password = undefined
        // }
        mutation.mutate(data)
    }

    const onCancel = () => {
        reset()
        onClose()
    }

    return (
        <>
            <Modal
                isOpen={isOpen}
                onClose={onClose}
                size={{ base: "sm", md: "md" }}
                isCentered
            >
                <ModalOverlay />
                <ModalContent as="form" onSubmit={handleSubmit(onSubmit)}>
                    <ModalHeader>Edit User</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody pb={6}>
                        <FormControl isInvalid={!!errors.emp_email}>
                            <FormLabel htmlFor="email">Email</FormLabel>
                            <Input
                                id="email"
                                {...register("emp_email", {
                                    required: "Email is required",
                                    pattern: emailPattern,
                                })}
                                placeholder="Email"
                                type="email"
                            />
                            {errors.emp_email && (
                                <FormErrorMessage>{errors.emp_email.message}</FormErrorMessage>
                            )}
                        </FormControl>
                        <FormControl isInvalid={!!errors.emp_firstname}>
                            <FormLabel htmlFor="name">Name</FormLabel>
                            <Input
                                id="name"
                                {...register("emp_firstname", {
                                    required: "Name is required",
                                })}
                                placeholder="Name"
                                type="text"
                            />
                            {errors.emp_firstname && (
                                <FormErrorMessage>{errors.emp_firstname.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.position_id}>
                            <FormLabel htmlFor="position">Position</FormLabel>
                            <Input
                                id="position"
                                {...register("position_id", {
                                    required: "Position is required",
                                })}
                                placeholder="Position"
                                type="text"
                            />
                            {errors.position_id && (
                                <FormErrorMessage>{errors.position_id.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.department_id}>
                            <FormLabel htmlFor="department">Department</FormLabel>
                            <Input
                                id="department"
                                {...register("department_id", {
                                    required: "Department is required",
                                })}
                                placeholder="Department"
                                type="text"
                            />
                            {errors.department_id && (
                                <FormErrorMessage>{errors.department_id.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_phone}>
                            <FormLabel htmlFor="phone">Phone</FormLabel>
                            <Input
                                id="phone"
                                {...register("emp_phone", {
                                    required: "Phone is required",
                                })}
                                placeholder="Phone"
                                type="tel"
                            />
                            {errors.emp_phone && (
                                <FormErrorMessage>{errors.emp_phone.message}</FormErrorMessage>
                            )}
                        </FormControl>
                        <FormControl isInvalid={!!errors.emp_pin}>
                            <FormLabel htmlFor="pin">PIN</FormLabel>
                            <Input
                                id="pin"
                                {...register("emp_pin", {
                                    required: "PIN is required",
                                })}
                                placeholder="PIN"
                                type="text"
                            />
                            {errors.emp_pin && (
                                <FormErrorMessage>{errors.emp_pin.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_ssn}>
                            <FormLabel htmlFor="ssn">SSN</FormLabel>
                            <Input
                                id="ssn"
                                {...register("emp_ssn", {
                                    required: "SSN is required",
                                })}
                                placeholder="SSN"
                                type="text"
                            />
                            {errors.emp_ssn && (
                                <FormErrorMessage>{errors.emp_ssn.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_role}>
                            <FormLabel htmlFor="role">Role</FormLabel>
                            <Input
                                id="role"
                                {...register("emp_role", {
                                    required: "Role is required",
                                })}
                                placeholder="Role"
                                type="text"
                            />
                            {errors.emp_role && (
                                <FormErrorMessage>{errors.emp_role.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_lastname}>
                            <FormLabel htmlFor="lastname">Last Name</FormLabel>
                            <Input
                                id="lastname"
                                {...register("emp_lastname", {
                                    required: "Last Name is required",
                                })}
                                placeholder="Last Name"
                                type="text"
                            />
                            {errors.emp_lastname && (
                                <FormErrorMessage>{errors.emp_lastname.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_username}>
                            <FormLabel htmlFor="username">Username</FormLabel>
                            <Input
                                id="username"
                                {...register("emp_username", {
                                    required: "Username is required",
                                })}
                                placeholder="Username"
                                type="text"
                            />
                            {errors.emp_username && (
                                <FormErrorMessage>{errors.emp_username.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_pwd}>
                            <FormLabel htmlFor="password">Password</FormLabel>
                            <Input
                                id="password"
                                {...register("emp_pwd", {
                                    required: "Password is required",
                                })}
                                placeholder="Password"
                                type="password"
                            />
                            {errors.emp_pwd && (
                                <FormErrorMessage>{errors.emp_pwd.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_timezone}>
                            <FormLabel htmlFor="timezone">Timezone</FormLabel>
                            <Input
                                id="timezone"
                                {...register("emp_timezone", {
                                    required: "Timezone is required",
                                })}
                                placeholder="Timezone"
                                type="text"
                            />
                            {errors.emp_timezone && (
                                <FormErrorMessage>{errors.emp_timezone.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_payroll_id}>
                            <FormLabel htmlFor="payroll_id">Payroll ID</FormLabel>
                            <Input
                                id="payroll_id"
                                {...register("emp_payroll_id", {
                                    required: "Payroll ID is required",
                                })}
                                placeholder="Payroll ID"
                                type="text"
                            />
                            {errors.emp_payroll_id && (
                                <FormErrorMessage>{errors.emp_payroll_id.message}</FormErrorMessage>
                            )}
                        </FormControl>

                        <FormControl isInvalid={!!errors.emp_payroll_type}>
                            <FormLabel htmlFor="payroll_type">Payroll Type</FormLabel>
                            <Input
                                id="payroll_type"
                                {...register("emp_payroll_type", {
                                    required: "Payroll Type is required",
                                })}
                                placeholder="Payroll Type"
                                type="text"
                            />
                            {errors.emp_payroll_type && (
                                <FormErrorMessage>{errors.emp_payroll_type.message}</FormErrorMessage>
                            )}
                        </FormControl>
                    </ModalBody>
                    <ModalFooter gap={3}>
                        <Button
                            variant="primary"
                            type="submit"
                            isLoading={isSubmitting}
                            isDisabled={!isDirty}
                        >
                            Save
                        </Button>
                        <Button onClick={onCancel}>Cancel</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
}

export default EditEmployee