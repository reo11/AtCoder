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

color = [-1 for _ in range(n)]
cnts = [0 for _ in range(2)]
def coloring(num, pre_color):
    if pre_color:
        col = 0
    else:
        col = 1
    color[num-1] = col
    cnts[col] += 1
    for k in edges[num].keys():
        if color[k-1] == -1:
            coloring(k, col)

coloring(1, 1)

ans = [0 for _ in range(n)]
def solve(v):
    for i in range(n):
        if color[i] == v:
            ans[i] = nums[0].pop()
        else:
            for j in [1, 2, 0]:
                if len(nums[j]) > 0:
                    ans[i] = nums[j].pop()
                    break

if cnts[0] <= n // 3:
    # print("A")
    solve(0)
elif cnts[1] <= n // 3:
    # print("B")
    solve(1)
else:
    # print("C")
    for i in range(n):
        if color[i]:
            if len(nums[1]) > 0:
                ans[i] = nums[1].pop()
            else:
                ans[i] = nums[0].pop()
        else:
            if len(nums[2]) > 0:
                ans[i] = nums[2].pop()
            else:
                ans[i] = nums[0].pop()

print(" ".join(list(map(str, ans))))