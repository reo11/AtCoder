import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
s = set()
for _ in range(n):
    si = input()
    reversed_si = si[::-1]
    if si in s or reversed_si in s:
        continue
    else:
        s.add(si)
# print(s)
print(len(s))