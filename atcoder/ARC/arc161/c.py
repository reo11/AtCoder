import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

def check(ans, ab, s):
    # ansを伝播させて、sと一致するか確認する
    # 一致しない場合は、-1を返す
    # 一致する場合は、ansを返す
    wb_counter = [[0 for _ in range(2)]for _ in range(n + 1)]
    edges = defaultdict(list)
    for a, b in ab:
        edges[a].append(b)
        edges[b].append(a)
    for i in range(1, n + 1):
        for edge in edges[i]:
            if ans[i - 1] == "W":
                wb_counter[edge][0] += 1
            else:
                wb_counter[edge][1] += 1
    ans_s = []
    for i in range(1, n + 1):
        if wb_counter[i][0] > wb_counter[i][1]:
            ans_s.append("W")
        else:
            ans_s.append("B")
    ans_s = "".join(ans_s)
    if ans_s == s:
        return ans
    else:
        return -1

def solve(n, ab, s):
    # 有向グラフで考える
    # 双方向の辺を貼る
    # 次元数が1の頂点の周辺から確定していく
    # 次元数1以上の頂点が残ったら、その頂点を中心に未確定の頂点にdemandを送り、多数決で決定
    edges = defaultdict(lambda: set())
    dims = defaultdict(int)
    dim_memo = defaultdict(lambda: set())
    for a, b in ab:
        edges[a].add(b)
        edges[b].add(a)
        dims[a] += 1
        dims[b] += 1
    for i in range(1, n + 1):
        dim_memo[dims[i]].add(i)
    ans = ["?" for _ in range(n)]
    while True:
        # print(ans)
        if len(dim_memo[1]) <= 0:
            break
        dim_solo = dim_memo[1].pop()
        for next_edge in edges[dim_solo]:
            if s[dim_solo - 1] == "W":
                if ans[next_edge - 1] != "?" and ans[next_edge - 1] != "W":
                    return -1
                ans[next_edge - 1] = "W"
            else:
                if ans[next_edge - 1] != "?" and ans[next_edge - 1] != "B":
                    return -1
                ans[next_edge - 1] = "B"
    # 次元数1がなくなった
    wb_counter = [[0 for _ in range(2)]for _ in range(n + 1)]
    l = []
    for i in range(1, n + 1):
        if ans[i - 1] == "?":
            l.append(i)
    for edge in l:
        for next_edge in edges[edge]:
            if s[edge - 1] == "W":
                wb_counter[next_edge][0] += 1
            else:
                wb_counter[next_edge][0] += 1
    for edge in l:
        if wb_counter[edge][0] > wb_counter[edge][1]:
            ans[edge - 1] = "W"
        else:
            ans[edge - 1] = "B"
    return "".join(ans)

ans = []
for _ in range(t):
    n = int(input())
    ab = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        ab.append((a, b))
    s = input()
    ans_i = solve(n, ab, s)
    if ans_i == -1:
        ans.append(ans_i)
    else:
        ans.append(check(ans_i, ab, s))
print(*ans, sep='\n')
