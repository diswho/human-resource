-- SELECT * FROM "att_DayType";

-- DROP TABLE IF EXISTS att_day_summary;
DROP TABLE IF EXISTS "att_daytype";
-- DROP TABLE IF EXISTS att_employee_shift 
-- DROP TABLE IF EXISTS att_punches;
-- DROP TABLE IF EXISTS att_shift_details;
-- DROP TABLE IF EXISTS att_shift;
-- DROP TABLE IF EXISTS "att_StatisticItem";
-- DROP TABLE IF EXISTS att_timetable;

-- DROP TABLE IF EXISTS hr_performance;
-- DROP TABLE IF EXISTS hr_salaries;
-- DROP TABLE IF EXISTS hr_deductions;
-- DROP TABLE IF EXISTS hr_payments;
-- DROP TABLE IF EXISTS deduction_types;
-- DROP TABLE IF EXISTS payment_types;

-- DROP TABLE IF EXISTS hr_employee;
-- DROP TABLE IF EXISTS hr_position;
-- DROP TABLE IF EXISTS hr_department;
-- DROP TABLE IF EXISTS hr_company;


-- INSERT INTO deduction_types (id, la_name, en_name, description) VALUES
--     (1, 'ພາສີລາຍໄດ້', 'Income Tax', 'Income tax deduction'),
--     (2, 'ປະກັນສັງຄົມ', 'Social Security', 'Social security contribution'),
--     (3, 'ກຸ່ມປະກັນໄພ', 'Insurance', 'Insurance premium deduction'),
--     (4, 'ກຸ່ມກູ້ຢືມ', 'Loan Repayment', 'Loan repayment deduction'),
--     (5, 'ເງີນລວງໜ້າ', 'Advance Deduction', 'Advance deduction'),
--     (6,'ການຫັກຄວາມເສຍຫາຍ','Damage Deduction','Deduction for damage caused by employee'),
--     (7,'ວັນຂາດ','Absenteeism','Deduction for unexcused absences'),
--     (8,'ການຫັກລະບຽບວິໄນ','Discipline Deduction','Deduction for disciplinary action'),
--     (9,'ການຫັກຄວາມສົນໃຈ','Charity Deduction','Deduction for charitable donations')
-- ;

-- INSERT INTO payment_types (id, en_name, la_name, description) VALUES
--     (1, 'Salary', 'ເງິນເດືອນ', 'Salary payment for employees'),
--     (2, 'Overtime', 'ລ່ວງເວລາ', 'Overtime payment for employees'),
--     (3, 'Bonus', 'ໂບນັດ', 'Bonus payment for employees'),
--     (4, 'Travel Allowance', 'ເງິນອຸດໜູນພາກສະໜາມ', 'Compensation for travel-related expenses incurred while performing job duties.'),
--     (5, 'Housing Allowance', 'ເງິນອຸດໜູນທີ່ຢູ່ອາໄສ', 'Housing Allowance payment for employees'),
--     (6,'COLA','ເງິນອຸດໜູນຄ່າຄອງຊີບ','Cost of Living Allowance payment for employees'),
--     (7,'Education Allowance','ເງິນອຸດໜູນການສຶກສາ','Education Allowance payment for employees'),    
--     (8,'Medical Allowance','ເງິນອຸດໜູນທາງການແພດ','Medical Allowance payment for employees'),
--     (9,'Transportation Allowance','ເງິນອຸດໜູນການເດີນທາງ','Covers commuting costs between home and work.'),
--     (10,'Food Allowance','ເງິນອຸດໜູນອາຫານ','Food Allowance payment for employees'),
--     (11,'Entertainment Allowance','ເງິນອຸດໜູນການບັນເທີງ','Reimbursement for expenses incurred while entertaining clients.'),
--     (12,'Internet and Mobile Allowances','ເງິນອຸດໜູນ ອີນເຕີເນັດ ແລະ ມືຖື','Extra payments during festive seasons or as performance incentives.'),
--     (13,'Bonus Allowance', 'ເງິນອຸດໜູນໂບນັດ', 'Bonus Allowance payment for employees'),
--     (14,'Sumptuary Allowance','ເງີນຮັບແຂກ','Provided to government officials for hosting visitors, varying by rank.'),
--     (15,'hard work Allowance','ເງິນຂະຫຍັນ','Hard work Allowance payment for employees')
-- ;