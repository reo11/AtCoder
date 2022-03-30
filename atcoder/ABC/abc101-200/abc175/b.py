from itertools import combinations

n = int(input())
l = list(map(int, input().split()))

def is_triangle(t):
    return sum(t) - max(t) > max(t)

cnt = 0
for t in combinations(range(n), 3):
    t = [l[x] for x in t]
    if len(set(t)) != 3:
        continue
    if is_triangle(t):
        cnt += 1
print(cnt)