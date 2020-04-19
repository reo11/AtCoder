n, m = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
if s > n:
    print(-1)
else:
    print(n - s)