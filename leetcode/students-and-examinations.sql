with student as (
select
a.*,
b.*
from Students a
cross join Subjects b
order by a.student_id
)

select
a.student_id,
a.student_name,
a.subject_name,
count(b.student_id ) as attended_exams
from student a
left join Examinations b on b.student_id = a.student_id
                        and b.subject_name = a.subject_name
group by 
a.student_id,
a.student_name,
a.subject_name
order by a.student_id, a.subject_name