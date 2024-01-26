from collections import defaultdict, deque

n, m = map(int, input().split())
s = list(input())
c = list(map(int, input().split()))

que = defaultdict(lambda: deque())

for si, ci in zip(s, c):
    que[ci].append(si)

# 最後を最初に持ってくる
for ci in que.keys():
    que[ci].appendleft(que[ci].pop())

ans = []

for ci in c:
    ans.append(que[ci].popleft())
print("".join(ans))
