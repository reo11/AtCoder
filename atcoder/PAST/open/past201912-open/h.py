import sys
from math import ceil
input = lambda: sys.stdin.readline().rstrip()
INF = 10**10

n = int(input())
c = list(map(int, input().split()))
q = int(input())

# 奇数、偶数の最小値を保持
odd_min = INF
even_min = INF
for i, v in enumerate(c, start=1):
    if i % 2:
        odd_min = min(odd_min, v)
    even_min = min(even_min, v)

# 奇数、偶数がどのくらい売れたかを記録しておく
cnt_num = [0 for _ in range(n)]
cnt_odd = 0
cnt_even = 0

for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        # やるだけ
        x = s[1] - 1
        a = s[2]
        if x % 2 == 0:
            nokori = c[x] - cnt_odd - cnt_num[x]
            if nokori >= a:
                if nokori == odd_min:
                    odd_min = nokori - a
                cnt_num[x] += a
        else:
            nokori = c[x] - cnt_even - cnt_num[x]
            if nokori >= a:
                if nokori == even_min:
                    even_min = nokori - a
                cnt_num[x] += a
    elif s[0] == 2:
        # 奇数で最小値を共有していればよい
        a = s[1]
        if odd_min >= a:
            cnt_odd += a
            odd_min -= a
    else:
        # 偶数で最小値を共有していればよい
        a = s[1]
        if min(even_min, odd_min) >= a:
            cnt_odd += a
            cnt_even += a
            odd_min -= a
            even_min -= a
ans = sum(cnt_num)
ans += cnt_even * (n // 2)
ans += cnt_odd * ceil(n / 2)
print(ans)