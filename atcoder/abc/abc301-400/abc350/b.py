n, q = map(int, input().split())
t = list(map(int, input().split()))

teeth = [True] * n

for ti in t:
    if teeth[ti - 1]:
        teeth[ti - 1] = False
    else:
        teeth[ti - 1] = True

print(sum(teeth))