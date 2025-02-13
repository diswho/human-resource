SELECT * FROM "sy_status";

-- INSERT INTO sy_status (id, name_en) VALUES
-- (1,'pending'),
-- (2,'approved'),
-- (3,'rejected'),
-- (4,'cancelled'),
-- (5,'updated'),
-- (6,'deleted'),
-- (7,'completed'),
-- (8,'draft'),
-- (9,'onprogress'),
-- (10,'submitted'),
-- (11,'active'),
-- (12,'initiated'),
-- (13,'inactive')
-- ;


-- INSERT INTO sy_type (id, name_en, name_la, description_en, type) VALUES
--     (1, 'Salary', 'ເງິນເດືອນ', 'Salary payment for employees','IN'),
--     (2, 'Overtime', 'ລ່ວງເວລາ', 'Overtime payment for employees','IN'),
--     (3, 'Bonus', 'ໂບນັດ', 'Bonus payment for employees','IN'),
--     (4, 'Travel Allowance', 'ເງິນອຸດໜູນພາກສະໜາມ', 'Compensation for travel-related expenses incurred while performing job duties.','IN'),
--     (5, 'Housing Allowance', 'ເງິນອຸດໜູນທີ່ຢູ່ອາໄສ', 'Housing Allowance payment for employees','IN'),
--     (6,'COLA','ເງິນອຸດໜູນຄ່າຄອງຊີບ','Cost of Living Allowance payment for employees','IN'),
--     (7,'Education Allowance','ເງິນອຸດໜູນການສຶກສາ','Education Allowance payment for employees','IN'),
--     (8,'Medical Allowance','ເງິນອຸດໜູນທາງການແພດ','Medical Allowance payment for employees','IN'),
--     (9,'Transportation Allowance','ເງິນອຸດໜູນການເດີນທາງ','Covers commuting costs between home and work.','IN'),
--     (10,'Food Allowance','ເງິນອຸດໜູນອາຫານ','Food Allowance payment for employees','IN'),
--     (11,'Entertainment Allowance','ເງິນອຸດໜູນການບັນເທີງ','Reimbursement for expenses incurred while entertaining clients.','IN'),
--     (12,'Internet and Mobile Allowances','ເງິນອຸດໜູນ ອີນເຕີເນັດ ແລະ ມືຖື','Extra payments during festive seasons or as performance incentives.','IN'),
--     (13,'Bonus Allowance', 'ເງິນອຸດໜູນໂບນັດ', 'Bonus Allowance payment for employees','IN'),
--     (14,'Sumptuary Allowance','ເງີນຮັບແຂກ','Provided to government officials for hosting visitors, varying by rank.','IN'),
--     (15,'hard work Allowance','ເງິນຂະຫຍັນ','Hard work Allowance payment for employees','IN'),
--     (16, 'ພາສີລາຍໄດ້', 'Income Tax', 'Income tax deduction','OUT'),
--     (17, 'ປະກັນສັງຄົມ', 'Social Security', 'Social security contribution','OUT'),
--     (18, 'ກຸ່ມປະກັນໄພ', 'Insurance', 'Insurance premium deduction','OUT'),
--     (19, 'ກຸ່ມກູ້ຢືມ', 'Loan Repayment', 'Loan repayment deduction','OUT'),
--     (20, 'ເງີນລວງໜ້າ', 'Advance Deduction', 'Advance deduction','OUT'),
--     (21,'ການຫັກຄວາມເສຍຫາຍ','Damage Deduction','Deduction for damage caused by employee','OUT'),
--     (22,'ວັນຂາດ','Absenteeism','Deduction for unexcused absences','OUT'),
--     (23,'ການຫັກລະບຽບວິໄນ','Discipline Deduction','Deduction for disciplinary action','OUT'),
--     (24,'ການຫັກການກຸສົນ','Charity Deduction','Deduction for charitable donations','OUT')
-- ;


-- UPDATE sy_type SET name_la = 'ການຫັກການກຸສົນ' WHERE id = 24;


-- DROP TABLE IF EXISTS att_day_summary;
-- DROP TABLE IF EXISTS "att_daytype";
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



