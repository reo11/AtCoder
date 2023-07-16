from collections import defaultdict

n, x = map(int, input().split())
a = list(map(int, input().split()))

counter = defaultdict(lambda: 0)
for a_i in a:
    counter[a_i + x] += 1

ans = 0
for a_i in a:
    ans += counter[a_i]

if ans > 0:
    print("Yes")
else:
    print("No")
