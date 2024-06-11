CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
-- 函数体
DECLARE M INT;
    SET M = N-1;
-- 函数体
  RETURN (
--       返回值
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT M, 1
--       返回值
  );
END

-- LIMIT M, 1 从M开始，取下一行的。若1改为2则取下两行，以此类推
-- limit N : 返回 N 条记录
-- offset M : 跳过 M 条记录, 默认 M=0, 单独使用似乎不起作用
-- limit N,M : 相当于 limit M offset N , 从第 N 条记录开始, 返回 M 条记录