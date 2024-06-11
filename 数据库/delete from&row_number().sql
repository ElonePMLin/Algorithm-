-- 简洁的写法，删除重复且大的id
delete p1 from Person p1, Person p2  -- 这种写法能保证where中不用建立临时表来取Person数据
where p1.email = p2.email and p1.id > p2.id;

-- 窗口函数方法
delete from Person  -- 这种方法where中必须 在临时表中才能取Person数据，否则报错
where id in (
    select id
    from (
        select
            id,
            row_number() over (partition by email order by id) as num
        from Person
    ) tmp
    where tmp.num > 1
)
