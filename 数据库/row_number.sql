-- 连续出现大于三次
SELECT *
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;

-- 上述方法，太过耦合，4次，5次，1000次

-- 第三部、将取得值，仅取Num列即为答案
SELECT DISTINCT Num as ConsecutiveNums
FROM (
    SELECT Num, COUNT(1) as SerialCount
    FROM (
        -- 第一步、计算 Num 和 连续 Num 的标识符
        SELECT Id,Num,
        row_number() over(order by id) - -- row_number() 为生成每行的num。与 dense_rank() 一样也是窗口函数。
        row_number() over(partition by Num order by Id) as SerialNumberSubGroup  -- 以num为一组独立进行处理，
                                                                                 -- 即（1，1，1 -- 1，2，3；2，2 -- 1，2）
        FROM Logs
        ) as Sub
    -- 第二步、以Num 和 SerialNumberSubGroup 为组，统计起分组的数量，且取数值大于等于3的 Num 和 其数值
    GROUP BY Num,SerialNumberSubGroup HAVING COUNT(1) >= 3
    ) as Result


select distinct num as ConsecutiveNums
from (
    select
        num,
        row_number() over(order by id) - row_number() over(partition by num order by id) as consecutive
    from Logs
) as consec  -- 临时表必须有别名
group by num, consecutive having count(1) >= 3
