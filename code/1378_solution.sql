# Write your MySQL query statement below
select unique_id, name
from employees emp left join employeeuni uni on emp.id = uni.id;
