import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

MAX = 10**9

def sep(n):
    # エジプト分数
    return [n + 1, n * (n + 1)]

def solve():
    n = int(input())
    v = []
    q = deque()
    q.append(1)
    checked = set([1])
    count = 1
    while len(q) > 0 and count < n:
        num = q.popleft()
        n1, n2 = sep(num)
        if n1 > MAX or n2 > MAX:
            v.append(num)
            continue
        if n1 in checked or n2 in checked:
            # どちらかが既に入っている場合重複してしまうので処理しない
            v.append(num)
            continue
        if n1 == n2:
            # num = 1のケースで発生する
            # n3を作って解消
            n2, n3 = sep(n2)
            checked.discard(num)
            q.append(n1)
            q.appendleft(n2)
            q.appendleft(n3)
            checked.add(n1)
            checked.add(n2)
            checked.add(n3)
        else:
            checked.discard(num)
            q.append(n1)
            q.appendleft(n2)
            checked.add(n1)
            checked.add(n2)
        count = len(checked)
    ans = []
    for i in range(len(v)):
        ans.append(v[i])
    for j in range(len(q)):
        ans.append(q[j])
    ans.sort()
    if len(ans) == n:
        return "Yes\n" + " ".join(map(str, ans))
    else:
        return "No"

t = int(input())
ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')