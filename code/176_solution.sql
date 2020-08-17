# Write your MySQL query statement below

select max(t.salary) as secondhighestsalary 
from (
    select * from employee 
    where salary < (select max(salary) from employee)
) as t;

