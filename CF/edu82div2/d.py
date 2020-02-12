from math import log2, ceil
t = int(input())
MAX_N = 64

for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n > sum(a):
        print(-1)
        continue

    needs = [0 for _ in range(MAX_N)]
    bits = [0 for _ in range(MAX_N)]

    while n > 0:
        x = int(log2(n))
        n -= 2**x
        needs[x] += 1

    for i in range(m):
        bits[int(log2(a[i]))] += 1

    ans = 0
    for i in range(MAX_N-1):
        if needs[i] > 0:
            for j in range(i, MAX_N-1):
                if bits[j] > 0:
                    bits[j] -= 1
                    needs[i] = 0
                    ans += j - i
                    for k in range(i, j):
                        bits[k] += 1
                    break
        bits[i+1] += bits[i] // 2
    print(ans)
