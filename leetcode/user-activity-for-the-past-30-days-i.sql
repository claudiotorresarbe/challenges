/* Write your PL/SQL query statement below */
select
to_char(activity_date,'yyyy-mm-dd') as day,
count(distinct user_id) as active_users
from Activity a
where 1 = 1
and activity_date > to_date(to_char('2019-06-27')) 
and activity_date <= to_date(to_char('2019-07-27'))
and activity_type in('open_session', 'end_session', 'scroll_down','send_message')
group by activity_date
order by activity_date asc