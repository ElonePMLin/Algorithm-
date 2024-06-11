-- # Write your MySQL query statement below

-- dense_rank() over ()  专门为排行设置的，且不会存在间隙排名，即1，1，2，3 而不是 1，1，3，4
select
    score,
    dense_rank() over (
        order by S.score desc
    ) as 'rank'
from Scores as S;

-- 方法二：使用 COUNT(DISTINCT ...) 的相关子查询
SELECT
  S1.score,
  (
    SELECT
      COUNT(DISTINCT S2.score)
    FROM
      Scores S2
    WHERE
      S2.score >= S1.score
  ) AS 'rank'  -- 与下面同理，COUNT(DISTINCT S2.score) == S2.score >= S1.score 的个数 4 >= 4 个数 1， 4 >= 3.85 个数 2，是以S2 总数为准的统计个数，因此需要对S2去重
FROM
  Scores S1
ORDER BY
  S1.score DESC;

-- 方法三：使用 INNER JOIN 和 COUNT(DISTINCT...)
SELECT
  S.score,
  COUNT(DISTINCT T.score) AS 'rank'  -- S.score 满足 S.score <= T.score 的个数
FROM
  Scores S
  INNER JOIN Scores T ON S.score <= T.score
GROUP BY
  S.id,
  S.score
ORDER BY
  S.score DESC;

-- select * 的情况  -- S.score 满足 S.score <= T.score 的个数，且 T 去重，若无去重，4 <= 4 有两个
-- 4 <= 4 1个， 3.85 <= 4 2个 ... 以此为rank
-- | id | score | id | score |
-- | -- | ----- | -- | ----- |
-- | 5  | 4     | 3  | 4     |
-- | 3  | 4     | 3  | 4     |
-- | 4  | 3.85  | 3  | 4     |
-- | 6  | 3.65  | 2  | 3.65  |
-- | 2  | 3.65  | 2  | 3.65  |
-- | 1  | 3.5   | 1  | 3.5   |

-- 如果面试官要求不使用现代 SQL 工具（如窗口函数）来解决问题，
-- 使用 方法 2 或 方法 3 也是适当的策略。
-- 在这种情况下，方法 2 可能传达对 SQL 查询处理方式的更深入理解，
-- 而 方法 3 可能传达解决问题的创造性。
-- 无论哪种情况，都传达了一种积极和值得欢迎的特质。
