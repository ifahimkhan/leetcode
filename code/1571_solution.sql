# Write your MySQL query statement below
select 
    name as warehouse_name, 
    sum(product_volume * units) as volume
from 
    warehouse join (select product_id, width * length * height as product_volume
                    from products) as product_volume 
    on warehouse.product_id = product_volume.product_id
group by name;
