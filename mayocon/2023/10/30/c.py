import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
t = [int(input()) for _ in range(n)]

# tのlcm

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

ans = 1
for ti in t:
    ans = lcm(ans, ti)

print(ans)