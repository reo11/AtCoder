import sys
import copy
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, t, m = map(int, input().split())
ng_list = defaultdict(lambda: set())
for _ in range(m):
    a, b = map(int, input().split())
    ng_list[a].add(b)
    ng_list[b].add(a)

ans = 0
q = deque([[[], 1]])
while q:
    teams, current_member = q.popleft()
    # print(teams, current_member)
    if current_member > n:
        if len(teams) == t:
            ans += 1
        continue

    # 既存のチームに追加できるか確認
    for i in range(len(teams)):
        flag = True
        for member in teams[i]:
            if member in ng_list[current_member]:
                flag = False
                break
        if flag:
            ts = copy.deepcopy(teams)
            ts[i].append(current_member)
            q.appendleft([ts, current_member + 1])

    # 新しいチームを作成
    if len(teams) < t:
        ts = copy.deepcopy(teams)
        ts.append([current_member])
        q.appendleft([ts, current_member + 1])

print(ans)




