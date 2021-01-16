-- SELECT COALESCE(NULL, NULL, NULL, 'W3Schools.com', NULL, 'Example.com')
/*
COALESCE(x,y,z) = x if x is not NULL
  COALESCE(x,y,z) = y if x is NULL and y is not NULL
  COALESCE(x,y,z) = z if x and y are NULL but z is not NULL
  COALESCE(x,y,z) = NULL if x and y and z are all NULL
*/
-- mobile이 NULL값이면 010-0000-0000으로 대체해라!
SELECT name,
       COALESCE(mobile, '010-0000-0000')
FROM teacher

-- 비슷한 함수 : IFNULL(f1, f2)
/*
 IFNULL(x,y) = x if x is not NULL
  IFNULL(x,y) = y if x is NULL
*/
SELECT name,
       IFNULL(mobile, '010-0000-0000')
FROM teacher
