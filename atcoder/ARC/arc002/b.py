from datetime import datetime, timedelta

y, m, d = map(int, input().split("/"))
date = datetime(y, m, d)
print(date)
while True:
    y = date.year
    m = date.month
    d = date.day
    if y % (m * d) == 0:
        y = str(y).zfill(4)
        m = str(m).zfill(2)
        d = str(d).zfill(2)
        print("{}/{}/{}".format(y, m, d))
        exit()
    else:
        date += timedelta(days=1)
