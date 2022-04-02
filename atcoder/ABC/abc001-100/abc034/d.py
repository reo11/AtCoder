n, k = map(int, input().split())
wp = [list(map(int, input().split())) for _ in range(n)]


def check(target_per):
    l = []
    for w, p in wp:
        l.append([(p - target_per) * w / 100, w, p])
    l.sort(reverse=True)
    water = 0
    solt = 0
    for _, w, p in l[:k]:
        s = w * p / 100
        water += w - s
        solt += s
    ret = False
    per = solt / (water + solt) * 100
    if per >= target_per:
        ret = True
    return ret


l = 0
r = 100
while (r - l) > 10 ** (-9):
    mid = (r + l) / 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)
