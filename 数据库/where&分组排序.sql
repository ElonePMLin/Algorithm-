SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
--              可以用这个 AND e1.DepartmentId = e2.DepartmentId 来进行分组处理 并获取需要的数据
                AND e1.DepartmentId = e2.DepartmentId
        )
;

-- 上述是优化后更简洁的写法
-- 下面是自己想的，缺点多了一个临时表
-- 优化方案是将 排序的临时表放在 where中进行取值
select Department, Employee, Salary
from (
    select
        d.name Department,
        e1.name Employee,
        e1.salary Salary,
        (
            select count(distinct e2.salary)
            from Employee e2
            where e1.departmentId = e2.departmentId and e1.salary <= e2.salary
        ) ranks
    from Employee e1
    left join Department d on e1.departmentId = d.id
) rank_table
where ranks <= 3