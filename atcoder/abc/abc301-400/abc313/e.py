MOD = 998244353
n = int(input())
s = list(map(int, list(input())))
# 最初の数字以外が1であることが収束の条件
# なので2以降が1の場合のみを考える
# ?1*?の形式

# 条件を満たすか確認
flag = True
ans = 0
for i in range(n - 1):
    if s[i] > 1 and s[i + 1] > 1:
        flag = False

if not flag:
    print(-1)
    exit()
else:
    # 1の個数を数える
    t = 1
    for i in reversed(range(1, n)):
        if s[i] != 1:
            t += (t * (s[i] - 1)) % MOD
            t %= MOD
        t += 1
        t %= MOD
        # print(t)
    print(t - 1)