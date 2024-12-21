CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(100),
    position VARCHAR(100), 
    salary DECIMAL(10, 2), 
    hire_date DATE
);

CREATE TABLE employee_audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    name VARCHAR(100),
    position VARCHAR(100), 
    salary DECIMAL(10, 2), 
    hire_date DATE,
    action_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO employees (name, position, salary, hire_date) 
VALUES 
    ('John Doe', 'Software Engineer', 80000.00, '2022-01-15'),
    ('Jane Smith', 'Project Manager', 90000.00, '2021-05-22'),
    ('Alice Johnson', 'UX Designer', 75000.00, '2023-03-01');
    

DELIMITER $$
CREATE TRIGGER after_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit (employee_id, name, position, salary, hire_date)
    VALUES (NEW.employee_id, NEW.name, NEW.position, NEW.salary, NEW.hire_date);
END$$
DELIMITER ;

INSERT INTO employees (name, position, salary, hire_date) 
VALUES ('Michael Brown', 'QA Engineer', 70000.00, '2023-07-15');

select * from employee_audit

DELIMITER $$
CREATE PROCEDURE add_employee (
    IN emp_name VARCHAR(100), 
    IN emp_position VARCHAR(100), 
    IN emp_salary DECIMAL(10, 2), 
    IN emp_hire_date DATE)
BEGIN
    -- Insert into employees table
    INSERT INTO employees (name, position, salary, hire_date) 
    VALUES (emp_name, emp_position, emp_salary, emp_hire_date);
    
    -- Log the action in employee_audit table
    INSERT INTO employee_audit (employee_id, name, position, salary, hire_date)
    SELECT employee_id, name, position, salary, hire_date
    FROM employees
    WHERE name = emp_name AND position = emp_position;
END$$
DELIMITER ;

CALL add_employee('Emily Davis', 'Data Analyst', 65000.00, '2024-01-10');

select * from employees;
select * from employee_audit;
