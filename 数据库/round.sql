# Write your MySQL query statement below

select round(
    mul.num / count(total.num), 2
) fraction
from (
    select count(*) num
    from Activity A
    where (player_id, event_date) in (
        select player_id, date_add(min(event_date), interval +1 day) event_date
        from Activity
        group by player_id
    )
) mul, (
    select count(*) num
    from Activity
    group by player_id
) total


-- 利用left join 和 inner join（join）的不同，该题为了获取总用户数，且符合条件的，采用left join，当不符合条件的会null
select round(
    sum(if(A2.event_date, 1, 0)) / count(*), 2
) fraction
from (
    select player_id, min(event_date) event_date
    from Activity
    group by player_id
) A1
left join Activity A2 on (
    A1.player_id = A2.player_id and A1.event_date = date_add(A2.event_date, interval -1 day)
)

