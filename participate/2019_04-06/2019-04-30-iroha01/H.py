n = str(input())
ans = 0

sum_n = 0
for v in n[::-1]:
    sum_n += int(v)

while sum_n >= 10:
    ans = ans*10 + 9
    sum_n -= 9
ans = ans*10 + sum_n
ans = int(str(ans)[::-1])
if ans != int(n):
    print(ans)
else:
    if str(ans)[0] == '9':
        ans = "18" + str(ans)[1:]
    elif ans < 10:
        ans = "1" + str(int(str(ans)[0]) - 1) + str(ans)[1:]
    else:
        ans = str(int(str(ans)[0]) + 1) + str(int(str(ans)[1]) - 1) + str(ans)[2:]
    print(ans)
