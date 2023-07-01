from collections import defaultdict
n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))

s = 0

price = defaultdict(lambda: p[0])

for d_i, p_i in zip(d, p[1:]):
    price[d_i] = p_i

for c_i in c:
    s += price[c_i]
print(s)