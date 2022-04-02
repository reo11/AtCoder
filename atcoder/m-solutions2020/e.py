import sys

input = sys.stdin.readline

n = int(input())
xyp = []
ans = []
for _ in range(n):
    x, y, p = map(int, input().split())
    xyp.append([x, y, p])


# 初期状態k=0
cost = 0
for i in range(n):
    x, y, p = xyp[i]
    cost += min(x, y) * p
ans.append(cost)

# # k=1~n-1
# for k in range(1, n):


# # k=nで絶対に0
# ans.append(0)
# print("\n".join(list(map(str, ans))))
