-- https://topsic-contest.jp/contests/practice/problems/practice001

SELECT
    DISTRICT_NAME as '都道府県名',
    TOTAL_AMT as '総人口'
FROM POPULATION
WHERE DISTRICT_CODE != 0 and DISTRICT_CODE % 1000 = 0
ORDER BY 2 DESC