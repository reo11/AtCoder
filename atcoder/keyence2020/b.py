import heapq
import sys

input = sys.stdin.readline

n = int(input())
query = []
for _ in range(n):
    x, l_ = map(int, input().split())
    query.append([x + l_, x - l_])

# 貪欲
heapq.heapify(query)

finish, start = heapq.heappop(query)
time = finish
count = 1
while len(query) > 0:
    finish, start = heapq.heappop(query)
    if start >= time:
        time = finish
        count += 1
    else:
        continue
print(count)
