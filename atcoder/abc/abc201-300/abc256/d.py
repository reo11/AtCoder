MAX = 2 * 10**5
n = int(input())

imos = [0 for _ in range(MAX + 1)]
lr = []
for _ in range(n):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r] -= 1

value = 0
for i in range(1, MAX + 1):
    value += imos[i]
    imos[i] = value

ans = []

status = [0, -1]
for i in range(1, MAX + 1):
    if status[0] == 0:
        if imos[i] > 0:
            status = [1, i]
    else:
        if imos[i] == 0:
            ans.append(f"{status[1]} {i}")
            status = [0, -1]
print(*ans, sep="\n")
