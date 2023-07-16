import collections
import math


# 試し割法
def trial_division(n):
    # 素因数を格納するリスト
    factor = []
    # 2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    # リストが空ならそれは素数
    if n == 1:
        return factor
    if not factor:
        return [n]
    else:
        factor.append(n)
        return factor


n = int(input())
kai = [0 for _ in range(n + 1)]
MOD = 10 ** 9 + 7
l = []

for i in range(1, n + 1):
    l.extend(trial_division(i))
c = collections.Counter(l)

s = 1
for key, value in c.items():
    s *= value + 1
    s %= MOD

print(s)
