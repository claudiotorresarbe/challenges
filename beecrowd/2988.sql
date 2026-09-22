select teams.name , count(teams.id) as matches,

count( CASE WHEN (team_1_goals > team_2_goals and teams.id = team_1)  or   (team_2_goals > team_1_goals and teams.id = team_2)  then 1 end ) as victories ,

count( case when (team_1_goals < team_2_goals and teams.id = team_1)  or   (team_2_goals < team_1_goals and teams.id = team_2) then 1 end ) as defeats ,

count( case when team_1_goals = team_2_goals then 1 end) as draws,

count( CASE WHEN (team_1_goals > team_2_goals and teams.id = team_1)  or   (team_2_goals > team_1_goals and teams.id = team_2)  then 1 end )* 3 +
count( case when (team_1_goals < team_2_goals and teams.id = team_1)  or   (team_2_goals < team_1_goals and teams.id = team_2) then 1 end ) * 0 +

count( case when team_1_goals = team_2_goals then 1 end) * 1 as score 

from teams teams

join matches matches ON teams.id = matches.team_1 or teams.id = matches.team_2

group by teams.id, teams.name

order by score DESC, teams.name ;