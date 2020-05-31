n = int(input())
xyc = [list(map(int, input().split())) for _ in range(n)]

# x, yでそれぞれ二分探索
INF = 10**12
l = - 10 ** 5
r = 10 ** 5
pre_cost = INF
cost = INF * 2
while 