k, x = map(int, input().split())

min_n = max(-1000000, x-k+1)
max_n = min(1000000, x+k-1)
ans = list(range(min_n, max_n+1))
ans = [str(x) for x in ans]
print(" ".join(ans))