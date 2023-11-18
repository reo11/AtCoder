n = int(input())
a = list(map(int, input().split()))

max_a = max(a)
ans = min(a)

for ai in a:
    if ai == max_a:
        continue
    ans = max(ans, ai)
print(ans)