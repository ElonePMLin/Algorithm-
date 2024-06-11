# Write your MySQL query statement below
SELECT id,
    CASE
        WHEN tree.id = (SELECT atree.id FROM tree atree WHERE atree.p_id is NULL)
        THEN 'Root'
        WHEN tree.id IN (SELECT DISTINCT atree.p_id FROM tree atree)
        THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM tree;


-- 另外一种解法
# Write your MySQL query statement below
select id, if(p_id is null, 'Root', 'Inner') type
from Tree
where id in (
    select distinct if(p_id is null, id, p_id) id
    from Tree
) union all (
    select id, 'Leaf' type
    from Tree
    where id not in (
        select distinct if(p_id is null, id, p_id) id
        from Tree
    )
)



# Write your MySQL query statement below
-- 两边之和大于第三边
select *,
    case when x + y > z and x + z > y and y + z > x
    then 'Yes'
    else 'No'
    end triangle


# Write your MySQL query statement below
-- 两边之和大于第三边
select *, if(x + y > z, if(x + z > y, if(y + z > x, 'Yes', 'No'), 'No'), 'No') triangle
from Triangle