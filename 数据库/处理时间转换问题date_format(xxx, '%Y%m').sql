# Write your MySQL query statement below
select
    date_format(trans_date, '%Y-%m') month,
    country,
    count(*) trans_count,
    count(if(state = 'approved', true, null)) approved_count,
    sum(amount) trans_total_amount,
    sum(if(state = 'approved', amount, 0)) approved_total_amount
from Transactions
group by year(trans_date), month(trans_date), country
