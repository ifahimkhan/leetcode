# Write your MySQL query statement below
select s1.score, count(distinct s2.score) as `rank`
from scores s1, scores s2
where s2.score >= s1.score
group by s1.Id
order by `rank`;
