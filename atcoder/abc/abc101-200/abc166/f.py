import sys
from collections import defaultdict

input = sys.stdin.readline

n, a, b, c = map(int, input().split())
d = {"A": a, "B": b, "C": c}
outputs = ["Yes"]
cnt = defaultdict(lambda: defaultfict(lambda: 0))
ss = []
for i in range(n):
    s = input()
    ss.append(s)
    cnt[s[0]] += 1
    cnt[s[1]] += 1

f = True
for i in range(n):
    s = ss[i]
    fir = s[0]
    sec = s[1]
    if d[fir] == 0 and d[sec] == 0:
        f = False
    if d[fir] > d[sec]:
        outputs.append(sec)
        d[fir] -= 1
        d[sec] += 1
    elif d[fir] == d[sec]:
        outputs.append(sec)
        d[fir] -= 1
        d[sec] += 1
    else:
        outputs.append(fir)
        d[fir] += 1
        d[sec] -= 1

if f:
    print("\n".join(outputs))
else:
    print("No")
