from collections import defaultdict

n, m, k = map(int, input().split())

# bit全探索っぽいことをする
patterns = []
for i in range(m):
    car = list(input().split())
    ci = int(car[0])
    if car[-1] == "o":
        ri = True
    else:
        ri = False
    ai = list(map(int, car[1:-1]))
    num = 0
    for j in ai:
        num += 2 ** (j - 1)
    patterns.append([num, ri])

def bit_count(x, y):
    return bin(x & y).count("1")

# bit全探索
ans = 0
for i in range(2 ** n):
    num = 0
    for j in range(n):
        if (i >> j) & 1:
            num += 2 ** j
    count = 0
    for pattern, flag in patterns:
        if (bit_count(num, pattern) >= k) == flag:
            count += 1
    if count == len(patterns):
        ans += 1
print(ans)
