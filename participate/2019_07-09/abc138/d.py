import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000000)

n, q = map(int, input().split())
ab = [[] for _ in range(n+1)]
p_num = [0] * (n+1)
ans = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    ab[a].append(b)
for _ in range(q):
    p, x = map(int, input().split())
    p_num[p] += x

def dfs(num, cur_count):
    cur_count += p_num[num]
    ans[num] = cur_count
    if len(ab[num]) <= 0:
        return
    for v in ab[num]:
        dfs(v, cur_count)

dfs(1, 0)

out = []
for i in range(1, n+1):
    out.append(str(ans[i]))
print(" ".join(out))
