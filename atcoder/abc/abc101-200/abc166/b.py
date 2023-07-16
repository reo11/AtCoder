n, k = map(int, input().split())
arr = [0 for _ in range(n)]

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for v in a:
        arr[v - 1] += 1
ans = 0
for i in arr:
    if i == 0:
        ans += 1
print(ans)
