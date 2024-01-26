from bisect import bisect_left, bisect_right
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

sorted_a = list(sorted(list(set(a))))
counter = defaultdict(int)
ans = []

for ai in a:
    num = len(sorted_a) - bisect_right(sorted_a, ai)
    counter[num] += 1

for i in range(n):
    ans.append(counter[i])

print(*ans, sep="\n")
