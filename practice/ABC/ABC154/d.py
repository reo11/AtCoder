n, k = map(int, input().split())
p = list(map(int, input().split()))
p = [(x+1) / 2 for x in p]

# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r

cs = cumsum(p)

ans = 0
for i in range(k, n+1):
    ans = max(ans, cs[i] - cs[i-k])

print(ans)