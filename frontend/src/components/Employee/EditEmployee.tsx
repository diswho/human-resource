import { EmployeePublic } from "../../client/models"

interface EditEmployeeProps {
    employee: EmployeePublic
    isOpen: boolean
    onClose: () => void
}