n, q = map(int, input().split())
s = input()
ren = [0]
for i in range(n - 1):
    if s[i] == s[i + 1]:
        ren.append(1)
    else:
        ren.append(0)

# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r


cum = cumsum(ren)

ans = []
lr = []
for _ in range(q):
    l, r = map(int, input().split())
    lr.append((l, r))
    ans.append(str(cum[r] - cum[l]))
print("\n".join(ans))
# 累積和っぽく
