from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(int)
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r

ans = 0
c_sum = cumsum(a)
for v in c_sum:
    ans += d[(m + (v % m)) % m]
    d[v%m] += 1
print(ans)