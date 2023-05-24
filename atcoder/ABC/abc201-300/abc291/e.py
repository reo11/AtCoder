import heapq
from collections import defaultdict, deque


def solve():
    n, m = map(int, input().split())
    edges = defaultdict(lambda: [])
    rev_edges = defaultdict(lambda: [])
    into_num = defaultdict(int)

    for _ in range(m):
        x, y = map(int, input().split())
        edges[x].append(y)
        rev_edges[y].append(x)
        into_num[y] += 1

    # 有向グラフの一筆書き探索問題と捉える
    # 一筆書き出来ればYesで、minからmaxの道筋を示せばよい、他はNo

    # 逆有効グラフから最小値の候補を見つける（最小値が一意に定まらない場合、No）
    min_edges = []
    dq = deque()
    dq.append(list(rev_edges.keys())[0])
    checked = defaultdict(lambda: False)
    while len(dq) > 0:
        current_edge = dq.popleft()
        checked[current_edge] = True
        if len(rev_edges[current_edge]) == 0:
            min_edge = current_edge
            break
        for next_edge in rev_edges[current_edge]:
            if not checked[next_edge]:
                dq.append(next_edge)

    def topological_sort1(G, into_num, n):
        q = deque()
        for i in range(1, n + 1):
            if into_num[i] == 0:
                q.append(i)

        ans = []
        while q:
            v = q.popleft()
            ans.append(v)
            for adj in sorted(G[v]):
                into_num[adj] -= 1
                if into_num[adj] == 0:
                    q.append(adj)
        return ans

    def topological_sort2(G, into_num, n):
        q = deque()
        for i in reversed(range(1, n + 1)):
            if into_num[i] == 0:
                q.append(i)

        ans = []
        while q:
            v = q.popleft()
            ans.append(v)
            for adj in reversed(sorted(G[v])):
                into_num[adj] -= 1
                if into_num[adj] == 0:
                    q.append(adj)
        return ans

    # なんか重いのでトポロジカルソートする
    tmp_into_num = into_num.copy()
    l = topological_sort1(edges, tmp_into_num, n)
    l2 = topological_sort2(edges, into_num, n)
    flag = True
    if l != l2:
        flag = False

    if not flag:
        print("No")
    else:
        print("Yes")
        ans = [[num, str(i)] for i, num in enumerate(l, start=1)]
        ans.sort()
        print(" ".join([x[1] for x in ans]))


solve()
