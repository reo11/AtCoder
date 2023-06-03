import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
cur = int(input())

ans = []
for i in range(n-1):
    a = int(input())
    out = ""
    if cur < a:
        out += "up "
        out += str(a - cur)
    elif cur > a:
        out += "down "
        out += str(cur - a)
    else:
        out += "stay"
    ans.append(out)
    cur = a
print("\n".join(ans))