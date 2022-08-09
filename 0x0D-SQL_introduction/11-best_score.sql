-- lists records based on conditions
select `score`, `name`
from `second_table`
where `score` >= 10
order by `score` desc;
