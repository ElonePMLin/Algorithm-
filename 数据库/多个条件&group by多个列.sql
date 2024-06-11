-- 自己写的，似乎不够好
# Write your MySQL query statement below
select round(sum(tmp.tiv_2016), 2) tiv_2016
from (
    select tiv.tiv_2015, I.tiv_2016, concat(I.lat, ',', I.lon) loaction
    from Insurance I
    left join (
        select tiv_2015
        from Insurance
        group by tiv_2015
        having count(tiv_2015) > 1
    ) tiv on I.tiv_2015 = tiv.tiv_2015
    group by loaction
    having count(loaction) = 1
) tmp
where tmp.tiv_2015 is not null


-- 参考代码
select round(sum(tiv_2016))
from Insurance
where (lat, lon) in (
    select lat, lon
    from Insurance
    group by lat, lon
    having count(*) = 1
) and (tiv_2015) in (
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(*) > 1
)
