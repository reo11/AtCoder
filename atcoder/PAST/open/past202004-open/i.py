import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))
ans = defaultdict(lambda: 0)


def battle(a, num):
    if len(a) == 1:
        ans[a[0]] = num - 1
        return
    new_a = []
    for i in range(0, len(a), 2):
        if a[i] > a[i + 1]:
            new_a.append(a[i])
            ans[a[i + 1]] = num
        else:
            new_a.append(a[i + 1])
            ans[a[i]] = num
    return new_a


new_a = a
for i in range(1, n + 2):
    # print(new_a)
    new_a = battle(new_a, i)
out = []
for i in range(2 ** n):
    out.append(str(ans[a[i]]))
print("\n".join(out))
