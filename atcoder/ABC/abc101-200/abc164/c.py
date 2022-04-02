import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
ans = set()
for i in range(n):
    s = str(input())
    ans.add(s)
print(len(ans))
