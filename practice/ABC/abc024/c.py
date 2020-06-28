n, d, k = map(int, input().split())
lr = []
for i in range(d):
    l, r = map(int, input().split())
    lr.append([l, r])

out = []
for i in range(k):
    s, t = map(int, input().split())
    # 右側へ
    if s < t:
        for i in range(d):
            l, r = lr[i]
            if l <= s <= r:
                s = r
            if s >= t:
                break
        out.append(str(i+1))
    # 左側へ
    else:
        for i in range(d):
            l, r = lr[i]
            if l <= s <= r:
                s = l
            if s <= t:
                break
        out.append(str(i+1))
print("\n".join(out))
