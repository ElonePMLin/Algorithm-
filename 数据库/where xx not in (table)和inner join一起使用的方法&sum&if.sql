# Write your MySQL query statement below
-- where xx not in （临时表）方法
SELECT Request_at as Day,
       ROUND(SUM(IF(T.status = 'completed', 0, 1)) / COUNT(T.status), 2) AS 'Cancellation Rate'
FROM Trips T
WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
      AND Client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
      and driver_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
GROUP BY Request_at


-- inner join 方法
# Write your MySQL query statement below
select
    T.request_at AS 'Day',
    round(
        sum(if(T.status = 'completed', 0, 1)) / count(T.status), 2
    ) AS 'Cancellation Rate'
from Trips T
inner join Users U1 on (T.client_id = U1.users_id and U1.banned = 'No')
inner join Users U2 on (T.driver_id = U2.users_id and U2.banned = 'No')
where T.request_at between '2013-10-01' AND '2013-10-03'
group by T.request_at