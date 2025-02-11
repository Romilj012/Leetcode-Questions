# Write your MySQL query statement below
SELECT COALESCE(
    (SELECT DISTINCT(salary)
    FROM Employee
    ORDER by salary desc
    LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary;