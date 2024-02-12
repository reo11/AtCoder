import math

t = int(input())

def solve(n, a, b):
    flag = True
    if a > n:
        flag = False
    n -= a
    if b > n * math.ceil(n / 2):
        flag = False
    if flag:
        return "Yes"
    else:
        return "No"

ans = []

for _ in range(t):
    n, a, b = map(int, input().split())
    ans.append(solve(n, a, b))

print(*ans, sep="\n")