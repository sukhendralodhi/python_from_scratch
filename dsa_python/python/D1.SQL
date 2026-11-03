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










