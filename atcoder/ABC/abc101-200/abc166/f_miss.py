import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

n, a, b, c = map(int, input().split())
l = [[a, "A"], [b, "B"], [c, "C"]]
d = defaultdict(lambda: defaultfict(lambda: 0))
outputs = defaultdict(lambda: [])
for i in range(n):
    s = input()
    d[s[0]][s[1]] += 1
    d[s[1]][s[0]] += 1

if [a, b, c].count(0) == 3:
    # 最低でも1回は走査があるはずなので
    print("No")
    exit()
elif [a, b, c].count(0) == 2:
    # 両方が0のところが発生すると死ぬ
    l.sort(reverse=True)
    fir = l[0][1]
    sec = l[1][1]
    third = l[2][1]
    name = "".join(sorted(fir, sec))

    outputs[name].append(sec)
    d[fir][sec] -= 1
    d[sec][fir] -= 1
    l[0][0] += 1
    l[1][0] -= 1
    for i in range(d[fir][sec] // 2):
        outputs[name].append(fir)
        d[fir][sec] -= 1
        d[sec][fir] -= 1
        outputs[name].append(sec)
        d[fir][sec] -= 1
        d[sec][fir] -= 1

    name = "".join(sorted(third, sec))
    outputs[name].append(third)
    d[third][sec] -= 1
    d[sec][third] -= 1
    l[0][0] += 1
    l[1][0] -= 1
    for i in range(d[sec][third] // 2):
        outputs[name].append(third)
        d[third][sec] -= 1
        d[sec][third] -= 1
        outputs[name].append(sec)
        d[third][sec] -= 1
        d[sec][third] -= 1

    name = "".join(sorted(third, fir))
    outputs[name].append(fir)
    d[third][fir] -= 1
    d[fir][third] -= 1
    l[0][0] += 1
    l[1][0] -= 1
    for i in range(d[fir][third] // 2):
        outputs[name].append(third)
        d[third][fir] -= 1
        d[fir][third] -= 1
        outputs[name].append(fir)
        d[third][fir] -= 1
        d[fir][third] -= 1

    if d[fir][sec] > 0:
        outputs[name].append(sec)
        d[third][fir] -= 1
        d[fir][third] -= 1
    if d[sec][third] > 0:
        outputs[name].append(third)
        d[third][fir] -= 1
        d[fir][third] -= 1

else:
    print("Yes")
    # 0とやりとりし続けて後で残りをやればok
