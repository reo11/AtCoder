n = int(input())
h = list(map(int, input().split()))

ans = 0
max_h = max(h)
for i in range(n):
    if h[i] == max_h:
        ans = i + 1
print(ans)
