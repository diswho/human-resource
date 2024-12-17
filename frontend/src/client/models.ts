export type Body_login_login_access_token = {
  grant_type?: string | null;
  username: string;
  password: string;
  scope?: string;
  client_id?: string | null;
  client_secret?: string | null;
};

export type HTTPValidationError = {
  detail?: Array<ValidationError>;
};

export type ItemCreate = {
  title: string;
  description?: string | null;
};

export type ItemPublic = {
  title: string;
  description?: string | null;
  id: string;
  owner_id: string;
};

export type ItemUpdate = {
  title?: string | null;
  description?: string | null;
};

export type ItemsPublic = {
  data: Array<ItemPublic>;
  count: number;
};

export type Message = {
  message: string;
};

export type NewPassword = {
  token: string;
  new_password: string;
};

export type Token = {
  access_token: string;
  token_type?: string;
};

export type UpdatePassword = {
  current_password: string;
  new_password: string;
};

export type UserCreate = {
  email: string;
  is_active?: boolean;
  is_superuser?: boolean;
  full_name?: string | null;
  password: string;
};

export type UserPublic = {
  email: string;
  is_active?: boolean;
  is_superuser?: boolean;
  full_name?: string | null;
  id: string;
};

export type UserRegister = {
  email: string;
  password: string;
  full_name?: string | null;
};

export type UserUpdate = {
  email?: string | null;
  is_active?: boolean;
  is_superuser?: boolean;
  full_name?: string | null;
  password?: string | null;
};

export type UserUpdateMe = {
  full_name?: string | null;
  email?: string | null;
};

export type UsersPublic = {
  data: Array<UserPublic>;
  count: number;
};

export type ValidationError = {
  loc: Array<string | number>;
  msg: string;
  type: string;
};

export type EmployeePublic = {
  emp_email: string;
  emp_pin: string;
  emp_ssn: string;
  emp_role: string;
  emp_firstname: string;
  emp_lastname: string;
  emp_username: string;
  emp_pwd: string;
  emp_timezone: string;
  emp_phone: string;
  emp_payroll_id: string;
  emp_payroll_type: string;
  emp_pin2: string;
  emp_photo: string;
  emp_privilege: string;
  emp_group: string;
  emp_hiredate: string; // date in ISO format
  emp_address: string;
  emp_active: number; // 0 or 1
  emp_firedate: string; // date in ISO format
  emp_firereason: string;
  emp_emergencyphone1: string;
  emp_emergencyphone2: string;
  emp_emergencyname: string;
  emp_emergencyaddress: string;
  emp_cardNumber: string;
  emp_country: string;
  emp_city: string;
  emp_state: string;
  emp_postal: string;
  emp_fax: string;
  emp_title: string;
  emp_hourlyrate1: string;
  emp_hourlyrate2: string;
  emp_hourlyrate3: string;
  emp_hourlyrate4: string;
  emp_hourlyrate5: string;
  emp_gender: number; // 0 or 1
  emp_birthday: string; // date in ISO format
  emp_operationmode: number; // 0 or 1
  emp_OtherName: string;
  emp_Line: string;
  emp_Passport: string;
  emp_MotobikeLicence: string;
  emp_CarLicence: string;
  emp_customName1: string;
  emp_customInfo1: string;
  emp_customName2: string;
  emp_customInfo2: string;
  IsSelect: number; // 0 or 1
  nationalID: string;
  emp_Verify: string;
  emp_ViceCard: string;
  department_id: number;
  position_id: number;
  id: number;
};
export type EmployeesPublic = {
  data: Array<EmployeePublic>;
  count: number;
};

export type HRDepartmentExport = {
  id: number;
  dept_code: number;
  dept_name: string;
  dept_parentcode: number;
  descendants: number[];
  level: number;
};
export type HRDepartmentPublic = {
  id: number;
  dept_code: number;
  dept_name: string;
  dept_parentcode: number;
  // children: { [key: string]: HRDepartmentPublic };
  children: {  };
  descendants: number[];
  level: number;
};

export type HRDepartmentsPublic = {
  data: Array<HRDepartmentPublic>;
  count: number;
};
