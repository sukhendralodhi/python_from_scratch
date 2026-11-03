SELECT * FROM employees
WHERE salary > 80000;

SELECT * FROM employees
WHERE first_name LIKE 'S%';

SELECT * FROM employees
WHERE department LIKE '%ine%';

SELECT * FROM employees
WHERE first_name LIKE 'M___';

SELECT * FROM employees
WHERE department IN('HR', 'Marketing');

SELECT first_name, salary FROM employees
ORDER BY salary DESC;

SELECT first_name, salary, department
FROM employees
ORDER BY department ASC, salary DESC;

SELECT first_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

SELECT first_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3 OFFSET 6;


SELECT * FROM employees
WHERE role IS NULL;

SELECT * FROM employees
WHERE role IS NOT NULL;

SELECT * FROM employees
ORDER BY hire_date DESC
LIMIT 1;

SELECT * FROM employees
WHERE department = 'Engineering'
ORDER BY salary ASC
LIMIT 2;

SELECT * FROM employees
ORDER BY salary ASC
LIMIT 2 OFFSET 6;

SELECT 
	COUNT(*) AS total_staff,
	MIN(salary) AS lowest_salary,
	MAX(salary) AS highest_salary,
	SUM(salary) AS total_payroll,
	AVG(salary) AS average_salary
FROM employees;












