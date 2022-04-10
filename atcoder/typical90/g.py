import sys
import bisect
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(20000000)
INF = 10 ** 12

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
q = int(input())
ans = ""

for i in range(q):
    b = int(input())

    left_idx = left = bisect.bisect_left(a, b)
    score = INF

    if left_idx < len(a):
        score = min(score, abs(b - a[left_idx]))

    if left_idx - 1 >= 0:
        score = min(score, abs(b - a[left_idx - 1]))
    ans += str(score)
    if i < q - 1:
        ans += "\n"

print(ans)
