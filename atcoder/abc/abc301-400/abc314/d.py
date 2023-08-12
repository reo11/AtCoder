import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)


n = int(input())
s = list(input())
q = int(input())
txc = []
status = 0 # 1: komoji, 2: oomoji
exclude_set = set()
for _ in range(q):
    t, x, c = input().split()
    t = int(t)
    x = int(x)
    if t == 1:
        s[x - 1] = c
        exclude_set.add(x - 1)
    elif t == 2:
        status = 1
        exclude_set = set()
    elif t == 3:
        status = 2
        exclude_set = set()

if status == 1:
    for i, si in enumerate(s):
        if i not in exclude_set:
            s[i] = si.lower()
elif status == 2:
    for i, si in enumerate(s):
        if i not in exclude_set:
            s[i] = si.upper()

print("".join(s))