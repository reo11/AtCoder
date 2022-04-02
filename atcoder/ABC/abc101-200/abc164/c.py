import sys

input = sys.stdin.readline

n = int(input())
ans = set()
for i in range(n):
    s = str(input())
    ans.add(s)
print(len(ans))
