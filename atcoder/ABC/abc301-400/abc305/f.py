import heapq
from collections import deque
n, m = map(int, input().split())
# 移動は最大2n回 <= 200
output_count = 0

def judge_output(v: int):
    print(v)

def judge_input():
    kv = input()
    if kv in ["OK", "-1"]:
        exit()
    kv = list(map(int, kv.split()))
    k = kv[0]
    v = kv[1:]
    return k, v

# 2分木を考えると、全ての辺を最大2回使うようにすれば2 * (n - 1)回程度で全ての頂点を訪れられる
# 深さ優先探索をする

dist_list = [-1 for _ in range(n + 1)]
q = deque([(0, 1, [])])
# [1からの距離、頂点番号, 経路（戻る時用）]
while output_count < 2 * n:
    dist, num, l = q.popleft()
    dist_list[num] = dist
    k, v = judge_input()
    # まだ訪れていない頂点を訪れる
    v = [i for i in v if dist_list[i] == -1]
    if len(v) == 0:
        next_v = l.pop() # 戻る
        q.append([dist - 1, next_v, l])
    else:
        next_v = v[0]
        q.append([dist + 1, next_v, l + [num]])
    judge_output(next_v)