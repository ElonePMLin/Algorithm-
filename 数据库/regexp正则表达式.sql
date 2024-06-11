# Write your MySQL query statement below
select *
from Users
where mail REGEXP '^[a-zA-Z][0-9A-Za-z_./-]*\\@leetcode\\.com$'
