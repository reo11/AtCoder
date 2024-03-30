n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []

for ai in a:
    if ai % k == 0:
        ans.append(ai // k)
print(*ans, sep=" ")