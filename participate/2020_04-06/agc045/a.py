import sys
input = lambda: sys.stdin.readline().rstrip()

ans = []
t = int(input())
for _ in range(t):
   a = solve()
   ans.append(a)
print("\n".join(ans))


def solve():
   n = int(input())
   a = list(map(int, input().split()))
   s = input()
   