import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
# A = 0, 0, 0, ..., 0でも最小値は2^(N-1)で増える
# k > 50くらいでnを超えるのでそれくらいまで考えればよい


def print_ans(ans):
    ans = list(map(lambda x: str(x) if x <= n else str(n), ans))
    print(" ".join(ans))


all_max = [n] * n
if k > 50:
    print_ans(all_max)
    exit()

# k < 50の時はimos法でO(N*k)くらいで求まりそう

for _ in range(k):
    pre_a = a[:]
    imos = [0 for _ in range(n + 1)]
    for i in range(n):
        left = max(0, i - pre_a[i])
        right = min(n, i + pre_a[i] + 1)
        imos[left] += 1
        imos[right] -= 1
    # process
    v = 0
    for i in range(n):
        v += imos[i]
        if v > n:
            v = n
        a[i] = v
print_ans(a)
