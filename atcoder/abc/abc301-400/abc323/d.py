import sys
from collections import defaultdict
from heapq import heappop, heappush, heapify
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
sc = []
counter = defaultdict(int)
queue = []
heapify(queue)

for _ in range(n):
    si, ci = map(int, input().split())
    counter[si] += ci
    heappush(queue, si)

ans = 0
while queue:
    si = heappop(queue)
    if counter[si] > 1:
        two_si = counter[si] // 2
        one_si = counter[si] % 2
        counter[si] = one_si
        counter[si * 2] += two_si
        heappush(queue, si * 2)

for k, v in counter.items():
    ans += v

print(ans)
