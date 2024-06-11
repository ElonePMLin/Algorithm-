# Write your MySQL query statement below
select id, count(*) num
from (
    select requester_id id
    from RequestAccepted
    union all (
        select accepter_id id
        from RequestAccepted
    )
) all_id
group by id
order by num desc
limit 1


-- union all 不合并重复的
-- union 合并重复的