mod = int(input())

ans = -1
num = 7
for i in range(1, mod + 1):
    if num % mod == 0:
        ans = i
        break
    num = (num * 10) % mod
    num = (num + 7) % mod
print(ans)
