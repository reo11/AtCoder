import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(100000000)
n = int(input())
edges = defaultdict(lambda: defaultdict(lambda: False))
for i in range(n - 1):
    a, b = map(int, input().split())
    edges[a][b] = True
    edges[b][a] = True

nums = [deque() for _ in range(3)]
for i in range(1, n + 1):
    nums[i % 3].append(i)

ans = [0 for _ in range(n)]


def dfs(idx, pre_3, pre_2, pre_1):
    if pre_1 == -1:
        if pre_1 % 3 == 2 and len(nums[1]) > 0:
            out = nums[1].pop()
        elif pre_1 % 3 == 1 and len(nums[2]) > 0:
            out = nums[2].pop()
        else:
            out = nums[0].pop()
    else:
        if pre_1 % 3 != 0:
            if pre_1 % 3 == 2 and len(nums[1]) > 0:
                out = nums[1].pop()
            elif pre_1 % 3 == 1 and len(nums[2]) > 0:
                out = nums[2].pop()
            else:
                if len(nums[0]) > 0:
                    out = nums[0].pop()
                else:
                    print(-1)
                    exit()
        else:
            if len(nums[1]) > 0:
                out = nums[1].pop()
            elif len(nums[2]) > 0:
                out = nums[2].pop()
            else:
                if len(nums[0]) > 0:
                    out = nums[0].pop()
                else:
                    print(-1)
                    exit()
    ans[idx - 1] = out
    for k in edges[idx].keys():
        if ans[k - 1] == 0:
            dfs(k, pre_2, pre_1, out)


for i in range(1, n + 1):
    if len(edges[i]) == 1:
        dfs(i, -1, -1, -1)
        break

print(" ".join(list(map(str, ans))))
