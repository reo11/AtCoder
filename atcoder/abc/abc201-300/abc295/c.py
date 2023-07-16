from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

counter = defaultdict(int)
for a_i in a:
    counter[a_i] += 1

ans = 0
for color, count in counter.items():
    ans += count // 2

print(ans)
