# Write your MySQL query statement below
select 
    sa.student_name as member_a, 
    sb.student_name as member_b, 
    sc.student_name as member_c
from schoolA sa, schoolB sb, schoolC sc
where 
    sa.student_name != sb.student_name and 
    sb.student_name != sc.student_name and 
    sc.student_name != sa.student_name and
    sa.student_id != sb.student_id and
    sb.student_id != sc.student_id and
    sc.student_id != sa.student_id;
