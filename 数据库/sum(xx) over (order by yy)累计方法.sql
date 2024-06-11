# Write your MySQL query statement below
--  rows  preceding
select person_name
from (
    select person_name, sum(weight) over (order by turn) acc
    from Queue
) acc
where acc <= 1000
order by acc desc
limit 1
