from collections import defaultdict

n, m = map(int, input().split())
ps = []
p = []
s = []
for i in range(m):
    p_, s_ = input().split()
    p.append(int(p_))
    s.append(str(s_))

ac = 0
pen = 0
d = defaultdict(int)
for p_, s_ in zip(p, s):
    if s_ == "WA":
        if d[p_] != -1:
            d[p_] += 1
        else:
            pass
    else:
        if d[p_] == -1:
            pass
        else:
            pen += d[p_]
            d[p_] = -1
            ac += 1
print(ac, pen)
