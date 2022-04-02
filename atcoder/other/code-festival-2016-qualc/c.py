n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
INF = 10 ** 12
MOD = 10 ** 9 + 7

arr = [[1, INF] for _ in range(n)]
cur_max = -1
for i in range(n):
    cur = t[i]
    if cur > cur_max:
        arr[i][0] = max(cur, arr[i][0])
        arr[i][1] = min(cur, arr[i][1])
        cur_max = cur
    else:
        arr[i][1] = min(cur, arr[i][1])

cur_max = -1
for i in reversed(range(n)):
    cur = a[i]
    if cur > cur_max:
        arr[i][0] = max(cur, arr[i][0])
        arr[i][1] = min(cur, arr[i][1])
        cur_max = cur
    else:
        arr[i][1] = min(cur, arr[i][1])

for i in range(n):
    if arr[i][0] > arr[i][1]:
        print(0)
        exit()

ans = 1
for i in range(n):
    ans *= arr[i][1] - arr[i][0] + 1
    ans %= MOD
print(ans)
