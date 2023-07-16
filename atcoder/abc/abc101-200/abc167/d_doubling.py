# ダブリングを使って解く
n, k = map(int, input().split())
a = list(map(int, input().split()))

cur = 0
pre_doubling = list(range(1, n + 1))
doubling = a[:]
while k > 0:
    if k & 1:
        cur = doubling[cur] - 1
    k >>= 1
    pre_doubling = doubling[:]
    for i in range(n):
        doubling[i] = pre_doubling[pre_doubling[i] - 1]
print(cur + 1)
