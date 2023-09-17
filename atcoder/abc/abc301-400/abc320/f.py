n, h = map(int, input().split())
x = list(map(int, input().split()))
pf = []

for _ in range(n - 1):
    p, f = map(int, input().split())

# DP
# 往路を考えるのだるいので、