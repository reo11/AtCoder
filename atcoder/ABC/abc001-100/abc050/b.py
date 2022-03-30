n = int(input())
t = list(map(int, input().split()))
m = int(input())

sum_t = sum(t)
for i in range(m):
    p, x = map(int, input().split())
    ans = sum_t - t[p-1] + x
    print(ans)
