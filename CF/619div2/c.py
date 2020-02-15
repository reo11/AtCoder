import sys
input = sys.stdin.readline

def solve(n, m):
    z = n - m
    g = m + 1
    k = int(z / g)
    ans = (n * (n + 1) // 2) - (k * (k + 1) // 2) * g - (k + 1) * (z % g)
    return int(ans)

t = int(input())
out = []
for i in range(t):
    n, m = map(int, input().split())
    out.append(solve(n, m))
print("\n".join(list(map(str, out))))