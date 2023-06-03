import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
p = [int(input()) for _ in range(n)]
buka = [[] for _ in range(n+1)]
num_chokudai = -1
for i, v in enumerate(p, start=1):
    if v == -1:
        num_chokudai = i
        continue
    buka[v].append(i)

tree_len = [-1 for _ in range(n+1)]
tree_range = [[0, 0] for _ in range(n+1)]
g_i = 0
def dfs(cur_len, num):
    global g_i
    tree_range[num][0] = g_i
    g_i += 1
    if buka[num] == 0:
        tree_len[num] = 0
        return cur_len
    tmp_len = cur_len
    for next_num in buka[num]:
        tmp_len += dfs(1, next_num)
    tree_len[num] = tmp_len - 1
    return tmp_len

dfs(1, num_chokudai)
for num in range(1, n+1):
    tree_range[num][1] = tree_range[num][0] + tree_len[num]

q = int(input())
ab = [list(map(int, input().split())) for _ in range(q)]
ans = []
for i in range(q):
    a, b = ab[i]
    a_idx = tree_range[a][0]
    out = "No"
    if tree_range[b][0] <= a_idx <= tree_range[b][1]:
        out = "Yes"
    ans.append(out)
# print(tree_len)
# print(tree_range)
print("\n".join(ans))