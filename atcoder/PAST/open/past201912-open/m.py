import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
monsters = []
for i in range(n):
    a, b = map(int, input().split())
    monsters.append((a, b, 0))
for i in range(m):
    a, b = map(int, input().split())
    monsters.append((a, b, 1))

# 決め打ち二分探索
# 0 <= ans <= 100000 あたりを誤差10^(-8)くらいで探索すれば良さそう


def check(target_power):
    l = []
    for weight, power, is_otasuke in monsters:
        l.append(((power / weight - target_power) * weight, weight, power, is_otasuke))
    l.sort(reverse=True)
    i = 0
    max_power = 0
    w = 0
    p = 0
    cnt_all = 0
    cnt_otasuke = 0
    while cnt_all < 5:
        if l[i][3] == 1:
            if cnt_otasuke >= 1:
                i += 1
                continue
            else:
                cnt_otasuke += 1
        w += l[i][1]
        p += l[i][2]
        cnt_all += 1
        i += 1
    calc_p = p / w
    return calc_p >= target_power


l = 0
r = 10 ** 6
while (r - l) > 10 ** (-8):
    mid = (r + l) / 2
    if check(mid):
        l = mid
    else:
        r = mid
print(l)
