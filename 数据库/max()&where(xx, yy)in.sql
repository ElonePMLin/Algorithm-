select
    Department.name 'Department',
    Employee.name 'Employee',
    Salary
from Employee
left join Department on Department.id = Employee.departmentId
where (Employee.departmentId, salary) in (
    select departmentId, max(salary)
    from Employee
    group by departmentId
)