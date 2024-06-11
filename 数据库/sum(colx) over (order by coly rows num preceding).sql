# Write your MySQL query statement below
with C1 as (
    select visited_on, sum(amount) over(order by visited_on rows 6 preceding) amount, last
    from (
        select visited_on, sum(amount) amount, date_add(visited_on, interval '-6' day) last
        from Customer
        group by visited_on
    ) tmp
)

select C1.visited_on, C1.amount, round(
    C1.amount / 7, 2
) average_amount
from C1
join Customer C2 on C1.last = C2.visited_on
group by C1.visited_on
