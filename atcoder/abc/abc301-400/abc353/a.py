n = int(input())
h = list(map(int, input().split()))

base_h = h[0]

ans = -1
for i in range(1, n):
    if base_h < h[i]:
        ans = i + 1
        break
print(ans)