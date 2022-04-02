import heapq

MOD = 998244353
n = int(input())
s = str(input())
want = {"R": [], "G": [], "B": []}
for c in want.keys():
    want["R"] = [[0, i] for i in range(n)]

l = [[] for _ in range(n)]
for i in range(3 * n):
    if s[i] == "R":
        idx = heapq.heappop(want["R"], item)
