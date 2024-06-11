# Write your MySQL query statement below
SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student  -- COALESCE() 输出有值的一方
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id;



-- 慢
# Write your MySQL query statement below

select id, student
from (
    select if(id = (
        select count(*) id
        from Seat
    ), id, id + 1) id, student
    from Seat
    where id % 2 != 0
) odd
union all (
    select id, student
    from (
        select id - 1 id, student
        from Seat
        where id % 2 = 0
    ) event
)
order by id
