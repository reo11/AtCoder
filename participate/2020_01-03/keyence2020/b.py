import sys
import heapq
input = sys.stdin.readline

n = int(input())
query = []
for i in range(n):
    x, l = map(int, input().split())
    query.append([x+l, x-l])

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
