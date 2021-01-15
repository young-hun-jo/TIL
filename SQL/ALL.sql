'''
<Table for example> - Table name : 'world'
name	continent	area	population	gdp
Afghanistan	Asia	652230	25500100	20343000000
Albania	Europe	28748	2831741	12960000000
Algeria	Africa	2381741	37100000	188681000000
Andorra	Europe	468	78115	3712000000
Angola	Africa	1246700	20609294	100990000000
'''

/* 8.List each continent and the name of the country that comes first alphabetically.*/
SELECT x.continent, x.name
FROM world AS x
WHERE x.name <= ALL(SELECT y.name
                    FROM world AS y
                    WHERE x.continent = y.continent)

/* 9.Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show name, continent and population. */
SELECT x.name, x.continent, x.population
FROM world AS x
WHERE 25000000 <= ALL(SELECT y.population
                      FROM world AS y
                      WHERE y.continent = x.continent)

/* 10.Some countries have populations more than three times that of any of their neighbours (in the same continent). Give the countries and continents.*/
SELECT x.name, x.continent
FROM world AS x
WHERE x.population >= ALL(SELECT 3*y.population
                          FROM world AS y
                          WHERE y.continent = x.continent
                          AND y.name != x.name)


                          