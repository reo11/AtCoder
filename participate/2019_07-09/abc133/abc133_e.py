import sys

sys.setrecursionlimit(1000000)

n, k = map(int, input().split())

node = [[] for _ in range(n)]
conect_count = [0 for _ in range(n)]
ans_num = [1 for _ in range(n)]

for i in range(n-1):
    a, b = map(int, input().split())
    conect_count[a-1] += 1
    conect_count[b-1] += 1
    node[a-1].append(b-1)
    node[b-1].append(a-1)

checked = [False for _ in range(n)]

def dfs(num, k_):
    if checked[num]:
        return
    if k_ <= 1:
        return
    ans_num[num] = k_ - 1
    checked[num] = True
    for i, n in enumerate(node[num]):
        dfs(n, k_ - 1 - i)

dfs(0, k+1)
an = 1
print(ans_num)
for a in ans_num:
    an = (an * a) % (10**9+7)

print(an)
