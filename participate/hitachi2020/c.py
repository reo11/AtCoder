from collections import deque, defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
n = int(input())
edges = defaultdict(lambda : defaultdict(lambda: False))
for i in range(n-1):
    a, b = map(int, input().split())
    edges[a][b] = True
    edges[b][a] = True

nums = [deque() for _ in range(3)]
for i in range(1, n+1):
    nums[i%3].append(i)

ans = [0 for _ in range(n)]
def dfs(step, idx, pre_3, pre_2, pre_1):
    pre_3_mod = pre_3 % 3
    if pre_3 == -1:
        if len(edges[idx]) > 2:
            out = nums[0].pop()
        elif len(nums[step%3]) > 0:
            out = nums[step%3].pop()
        else:
            for i in [1, 2, 0]:
                if len(nums[i]) > 0:
                    out = nums[i].pop()
                    break
    else:
        if pre_3_mod != 0:
            if len(nums[3 - (pre_3_mod)]) > 0:
                out = nums[3 - (pre_3_mod)].pop()
            else:
                if len(nums[0]) > 0:
                    out = nums[0].pop()
                else:
                    print(-1)
                    exit()
        else:
            if len(nums[0]) > 0:
                out = nums[0].pop()
            else:
                if len(nums[1]) > len(nums[2]) and len(nums[1]) > 0:
                    out = nums[1].pop()
                else:
                    out = nums[2].pop()
    ans[idx-1] = out
    for k in edges[idx].keys():
        if ans[k-1] == 0:
            dfs(step+1, k, pre_2, pre_1, out)

for i in range(1, n+1):
    if len(edges[i]) == 1:
        dfs(1, i, -1, -1, -1)
        break

print(" ".join(list(map(str, ans))))