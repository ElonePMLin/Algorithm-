# Write your MySQL query statement below
WITH r AS (-- 以每台服务器按时间状态排序 status_time  00:00:00 -> 23:59:59
    SELECT
        *,
        RANK() OVER (PARTITION BY server_id ORDER BY status_time, session_status) AS rk
    FROM
        Servers
)


SELECT
    floor(sum(TIMESTAMPDIFF(SECOND, a.status_time, b.status_time) / 3600 / 24)) AS total_uptime_days
FROM
    r AS a,
    r AS b
WHERE
    a.server_id = b.server_id AND a.session_status = 'start' AND a.rk = b.rk - 1

-- rank() 以相同server_id为组，且 status_time, session_status 进行 排序
-- timestampdiff(second, start, end)  以second为准，start，end计算时间戳的差值
--


with T as (
    select session_status,
    status_time,
    lead(status_time) over(partition by server_id order by status_time) next_status_time
    from Servers
)

select floor(sum(TIMESTAMPDIFF(SECOND, status_time, next_status_time))/86400) as total_uptime_days
from T
where session_status='start'

-- lead('column', offset 1)  偏移行数的窗口函数，默认偏移1行
