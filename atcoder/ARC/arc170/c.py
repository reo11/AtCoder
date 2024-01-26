MOD = 998244353
n, m = map(int, input().split())
s = list(map(int, input().split()))

ans = [-1 for _ in range(n)]

count = 0
for i in range(n):
    si = s[i]
    if si == 1:
        ans[i] = count
        count += 1
if count > m:
    print(0)
    exit()

ans_num = 1
print(ans)
for i in range(n):
    if ans[i] == -1:
        ans_num *= m - count + 1
        ans_num %= MOD
    else:
        count -= 1

print(ans_num)
