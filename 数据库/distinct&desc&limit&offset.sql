SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
-- 如果没有第 2 高的薪资，即表里可能只有一条记录，这个解答会被评测为 'Wrong Answer' 。

-- 为了克服这个问题，我们可以将其作为临时表。(临时表没有值默认为null)
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;

-- 或者使用IFNULL(xxx, val)函数 if xxx is null, output val
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
;

-- | id | salary |
-- | -- | ------ |
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
--
-- 取第二高工资