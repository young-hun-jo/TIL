/*
13.  List every match with the goals scored by each team as shown. This will use "CASE WHEN" which has not been explained in any previous exercises.
mdate	        team1	score1	team2	score2
1  July 2012	ESP	       4	 ITA	   0
10 June 2012	ESP	       1	 ITA	   1
10 June 2012	IRL	       1	 CRO	   3
...
Notice in the query given every goal is listed. If it was a team1 goal then a 1 appears in score1, otherwise there is a 0. You could SUM this column to get a count of the goals scored by team1. Sort your result by mdate, matchid, team1 and team2.
*/

-- LEFT JOJN 해주는 이유 : 골이 안나왔을 경기를 대비해 game 테이블 쪽으로 향해 LEFT JOIN!!!
-- 1. CASE WHEN 조건 THEN ELSE END 사용 풀이
SELECT game.mdate,
       game.team1,
       SUM(CASE WHEN game.team1 = goal.teamid THEN 1 ELSE 0 END) AS score1, 
       game.team2,
       SUM(CASE WHEN game.team2 = goal.teamid THEN 1 ELSE 0 END) AS score2
FROM game
 LEFT JOIN goal ON game.id = goal.matchid
GROUP BY game.mdate, game.team1, game.team2
ORDER BY game.mdate, goal.matchid, game.team1, game.team2

-- 2. IF(조건, True일 때 값, False일 때 값) 사용 풀이
SELECT game.mdate,
       game.team1,
       SUM(IF(game.team1 = goal.teamid, 1, 0)) AS score1,
       game.team2,
       SUM(IF(game.team2 = goal.teamid, 1, 0)) AS score2
FROM game
 LEFT JOIN goal ON game.id = goal.matchid
GROUP BY game.mdate, game.team1, game.team2
ORDER BY game.mdate, goal.matchid, game.team1, game.team2
