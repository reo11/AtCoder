from math import sqrt
d = int(input())

heiho = []

for i in range(1, int(sqrt(d)) + 100):
    heiho.append(i**2)

ans = float("inf")
for x in heiho:
    ansi = d - x
    if ansi < 0:
        continue
    elif ansi == 0:
        ans = 0
        break
    l = 0
    r = len(heiho)
    while r - l > 1:
        mid = (r + l) // 2
        if heiho[mid] > ansi:
            r = mid
        else:
            l = mid
    ans = min(ans, abs(ansi - heiho[l]))
    ans = min(ans, abs(ansi - heiho[r]))
print(ans)