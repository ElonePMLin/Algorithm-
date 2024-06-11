# self join is like outer join

select distinct s1.id, s1.visit_date, s1.people
from stadium s1, stadium s2, stadium s3
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
    and (
        (s2.id = s1.id + 1 and s3.id = s1.id + 2)
        or (s2.id = s1.id - 1 and s3.id = s1.id + 1)
        or (s2.id = s1.id - 1 and s3.id = s1.id - 2)
    )  -- 大于等于 3 行的意思
order by id asc


# Write your MySQL query statement below
select id, visit_date, people
from (
    select
        *,
        (id - row_number() over(order by id)) continues
    from Stadium
    where people >= 100
) tmp
where continues in (
    select tmp.continues
    from (
        select (id - row_number() over(order by id)) continues
        from Stadium
        where people >= 100
    ) tmp
    group by tmp.continues
    having count(*) >= 3
)
