-- 한 꺼번에 2개 이상의 변수의 중복제거된 값들만 추출하기 위해서 DISTINCT 아래와 같이 사용
SELECT DISTINCT a.company, a.num
FROM route AS a 
 INNER JOIN route AS b ON a.company = b.company AND a.num = b.num
WHERE a.stop = 115 AND b.stop = 137