import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = list(map(int, input().split()))

# ループがあるか見つけ、ループのサイズを見つける
# ループしている場合、残りのｋをループで割ったあまりに置き換える
INF = 10**12
cnt = [-1 for _ in range(n)]
cur = 0
size = INF
idx = 0

for i in range(k):
    if cnt[cur] != -1:
        size = i - cnt[cur]
        idx = i
        for j in range((k - idx) % size):
            next_idx = a[cur] - 1
            cur = next_idx
        print(cur + 1)
        exit()
    cnt[cur] = i
    next_idx = a[cur] - 1
    cur = next_idx
print(cur + 1)