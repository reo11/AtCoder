from collections import defaultdict, deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
p = [int(input()) for _ in range(n)]
buka = [[] for _ in range(n+1)]
num_chokudai = -1
for i, v in enumerate(p, start=1):
    if v == -1:
        num_chokudai = i
        continue
    buka[v].append(i)

q = int(input())
ab = [list(map(int, input().split())) for _ in range(q)]
ans = defaultdict(lambda: defaultdict(lambda: None))
query = defaultdict(lambda: [])
for i in range(q):
    a, b = ab[i]
    query[a].append(b)

# 上司のリストを持ちながらdfs
# def dfs(zyoshi_set, num):
#     for zyoshi in query[num]:
#         if zyoshi in zyoshi_set:
#             ans[num][zyoshi] = 'Yes'
#         else:
#             ans[num][zyoshi] = 'No'
#     if len(buka[num]) == 0:
#         return
#     for num_b in buka[num]:
#         next_zyoshi_set = zyoshi_set | set([num])
#         dfs(next_zyoshi_set, num_b)
# dfs(set(), num_chokudai)

# que = deque([(num_chokudai, set())])
# while len(que) > 0:
#     num, zyoshi_set = que.popleft()
#     # print(num, zyoshi_set)
#     for zyoshi in query[num]:
#         if zyoshi in zyoshi_set:
#             ans[num][zyoshi] = 'Yes'
#         else:
#             ans[num][zyoshi] = 'No'
#     if len(buka[num]) == 0:
#         continue
#     for num_buka in buka[num]:
#         que.append((num_buka, zyoshi_set | set([num])))

from collections import defaultdict, deque

v, n = map(int, input().split())
es = [[int(x) for x in input().split()] for _ in range(n)]

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1

q = deque(v1 for v1 in range(v) if ins[v1] == 0)
res = []
while q:
    v1 = q.popleft()
    res.append(v1)
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)

print(', '.join(res))

outs = []
for i in range(q):
    a, b = ab[i]
    outs.append(ans[a][b])

print("\n".join(outs))