n = int(input())
a = list(map(int, input().split()))

# O(N)
cnt = 0
starts = [0 for _ in range(n)]
for i, v in enumerate(a):
    next_idx = v + i + 1
    if next_idx < n:
        starts[next_idx] += 1
    if 0 <= i - v + 1 <= n - 1:
        cnt += starts[i - v + 1]
print(cnt)
