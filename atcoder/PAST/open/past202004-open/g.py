import sys
from collections import deque, defaultdict
input = lambda: sys.stdin.readline().rstrip()

q = int(input())
que = deque([])
ans = []
for i in range(q):
    query = input().split()
    if query[0] == '1':
        c = query[1]
        x = int(query[2])
        que.append((c, x))
    else:
        d = int(query[1])
        deleted = defaultdict(int)
        while len(que) > 0 and d != 0:
            if que[0][1] > d:
                c, x = que.popleft()
                deleted[c] += d
                que.appendleft((c, x - d))
                d = 0
            else:
                c, x = que.popleft()
                deleted[c] += x
                d -= x
        ans_i = 0
        for _, v in deleted.items():
            ans_i += v**2
        ans.append(ans_i)
print("\n".join(list(map(str, ans))))

