n = int(input())

amari = 0
made = 0
cnt = 0
for i in range(1, n+1):
    cnt += i
    if cnt >= n:
        made = i
        amari = cnt - n
        break

ans = []
for i in range(1, made+1):
    if i == amari:
        continue
    ans.append(str(i))
print("\n".join(ans))
