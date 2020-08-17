CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select e1.salary
      from (select distinct salary from employee) e1
      where (select count(*) 
             from (select distinct salary from employee) e2
             where e2.salary > e1.salary) = N - 1
      limit 1
  );
END

# works on MySQL 5.6
# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
# BEGIN
#   RETURN (
#       # Write your MySQL query statement below.
#       select salary
#       from employee
#       group by salary
#       order by salary
#       limit 1
#       offset N-1
#   );
# END
