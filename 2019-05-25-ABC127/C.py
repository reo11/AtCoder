n, m = map(int, input().split())
max_l = 0
min_r = 10**5
for i in range(m):
    l, r = map(int, input().split())
    max_l = max(max_l, l)
    min_r = min(min_r, r)
ans = min_r - max_l + 1
if ans < 0:
    ans = 0
print(min_r - max_l + 1)
