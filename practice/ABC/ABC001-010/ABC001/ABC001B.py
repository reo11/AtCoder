m = int(input())

ans = ""
if m < 100:
    ans = "00"
elif 100 <= m <= 5000:
    tmp = int(m / 100)
    if tmp < 10:
        ans = "0" + str(tmp)
    else:
        ans = str(tmp)
elif 6000 <= m <= 30000:
    ans = str(int((m // 1000) + 50))
elif 35000 <= m <= 70000:
    ans = str(int((((m // 1000) - 30) / 5) + 80))
else:
    ans = "89"
print(ans)
