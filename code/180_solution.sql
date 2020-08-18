# Write your MySQL query statement below

# select distinct l1.Num as consecutivenums
# from logs l1, logs l2, logs l3
# where l1.id = l2.id - 1 
#   and l2.id = l3.id - 1
#   and l1.num = l2.num
#   and l2.num = l3.num;
    
with tmp as (select num,
                    lead(num, 1) over (order by id) as lead1,
                    lead(num, 2) over (order by id) as lead2
             from logs)
select distinct(tmp.num) as consecutivenums
from tmp
where tmp.lead1 = tmp.lead2 
  and tmp.num = tmp.lead1;    
