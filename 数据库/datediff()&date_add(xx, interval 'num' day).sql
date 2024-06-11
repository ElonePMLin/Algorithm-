-- 541 ms
# Write your MySQL query statement below
select w1.id
from Weather w1, Weather w2
where datediff(w1.recordDate, w2.recordDate) = 1  and w1.Temperature - w2.Temperature > 0


-- 332 ms
# Write your MySQL query statement below
select w1.id
from Weather w1, Weather w2
where w1.recordDate = date_add(w2.recordDate, interval '1' day) and w1.Temperature - w2.Temperature > 0
