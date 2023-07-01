s = input()
n = int(input())

# 10^18 = 2^60 60桁の2進数
# 2進数表示にする
n_bin = []
n_tmp = n
while n_tmp > 0:
    n_bin.append(n_tmp % 2)
    n_tmp = n_tmp // 2
n_bin.reverse()

# 最小のsよりnが小さいか考える
s_tmp = "0b" + s.replace("?", "0")
if int(s_tmp, 2) > n:
    print(-1)
    exit()
elif int(s_tmp, 2) == n:
    print(n)
    exit()

ans = 0
s = list(s)
for i in range(len(s)):
    if s[i] == "1":
        ans += 2 ** (len(s) - i - 1)

for i in range(len(s)):
    if s[i] == "?":
        if ans + 2 ** (len(s) - i - 1) <= n:
            ans += 2 ** (len(s) - i - 1)

if ans <= n:
    print(ans)
else:
    print(-1)
