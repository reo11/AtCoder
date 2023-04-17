SELECT
    AGE_GRP.AGE_CODE as '年齢コード',
    AGE_GRP.AGE_NAME as '年齢階層名',
    SUM(SP_TIME_5) as '5時間未満',
    SUM(SP_TIME_6) as '5時間以上6時間未満',
    SUM(SP_TIME_7) as '6時間以上7時間未満',
    SUM(SP_TIME_8) as '7時間以上8時間未満',
    SUM(SP_TIME_9) as '8時間以上9時間未満',
    SUM(SP_TIME_9OVER) as '9時間以上'
FROM SLEEP_TIME_DTL
JOIN AGE_GRP on SLEEP_TIME_DTL.AGE_CODE = AGE_GRP.AGE_CODE
JOIN PREFECTURE on SLEEP_TIME_DTL.PF_CODE = PREFECTURE.PF_CODE
WHERE PREFECTURE.PF_NAME in ('北海道', '青森県', '岩手県', '宮城県', '福島県')
GROUP BY 1, 2
ORDER BY AGE_GRP.AGE_CODE