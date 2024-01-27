from collections import deque
n = int(input())
ab = []
stuck = deque()

for i in range(n):
    a, b = map(int, input().split())
    min_ab = min(a, b)
    max_ab = max(a, b)
    ab.append([min_ab, "a", i])
    ab.append([max_ab, "b", i])
ab.sort()

ans = False
for v, is_ab, i in ab:
    if is_ab == "a":
        stuck.append(i)
    else:
        if len(stuck) > 0 and stuck[-1] == i:
            stuck.pop()
        else:
            ans = True
            break

print("Yes" if ans else "No")