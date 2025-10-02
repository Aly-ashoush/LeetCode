select e1.name
from Employee  e1
join (

    select managerId,
        COUNT(id) AS direct_reports_count
    FROM Employee

    where managerId IS NOT NULL
    group by managerId 
    having count(managerId) >= 5
)as managers_with_enough_reports
on e1.id=managers_with_enough_reports.managerId 
