n, k = map(int, input().split())
a = list(map(int, input().split()))

visited = set()

# 1からkまでの和を求める
ans = (k * (k + 1)) // 2
for ai in a:
    if ai in visited:
        continue
    elif ai >= 1 and ai <= k:
        visited.add(ai)
        ans -= ai
print(ans)
