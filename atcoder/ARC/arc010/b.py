from datetime import datetime, timedelta

n = int(input())
md = set([input().rstrip() for _ in range(n)])

date = datetime(2012, 1, 1)

ans = 0
stack = 0
streak = 0
while date.year == 2012:
    is_holiday = False
    m = date.month
    d = date.day
    if date.weekday() >= 5:
        is_holiday = True
        if f"{m}/{d}" in md:
            stack += 1
    elif f"{m}/{d}" in md:
        is_holiday = True
    elif stack > 0:
        stack -= 1
        is_holiday = True

    if is_holiday:
        streak += 1
    else:
        streak = 0
        stack = 0
    date += timedelta(days=1)
    ans = max(ans, streak)
print(ans)
