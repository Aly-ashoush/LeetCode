# Write your MySQL query statement below
select e.employee_id , 
e.name , 
count(*)as reports_count , 
round(avg(ee.age)) as average_age
from Employees e
join Employees ee
on e.employee_id = ee.reports_to  
group by e.employee_id
order by e.employee_id