# Write your MySQL query statement below
select name, SUM(amount) as balance
from transactions left join users on users.account = transactions.account
group by transactions.account
having balance >= 10000;
