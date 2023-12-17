from decimal import Decimal
from heapq import heappush, heappop, heapify
INF = float('inf')
SEARCH_DEPTH = 100

n, d = map(int, input().split())
w = list(map(int, input().split()))
w = sorted(w, reverse=True)
w = [Decimal(x) for x in w]

def calc_v(xs):
    v = Decimal(0)
    mean = Decimal(sum(xs) / len(xs))
    for x in xs:
        v += (Decimal(x) - mean) ** 2
    return Decimal(v / len(xs))

def solve_greedy(w, d):
    # 分散が最小になるようなグループを選び続ける
    boxes = [0 for _ in range(d)]
    candidates = [[0, boxes]]
    for wi in w:
        tmp_candidates = []
        for c in candidates:
            tmp_boxes = c[1][:]
            processed_box = set()
            for i in range(d):
                if tmp_boxes[i] in processed_box:
                    continue
                processed_box.add(tmp_boxes[i])
                tmp_boxes[i] += wi
                tmp_v = calc_v(tmp_boxes)
                # print(i, tmp_boxes, tmp_v)
                heappush(tmp_candidates, [tmp_v, tmp_boxes[:]])
                tmp_boxes[i] -= wi
        candidates = []
        for _ in range(SEARCH_DEPTH):
            if len(tmp_candidates) == 0:
                break
            c = heappop(tmp_candidates)
            # print("a", c)
            candidates.append(c)
        # print(candidates)
    return candidates[0][1], candidates[0][0]

boxes, v = solve_greedy(w, d)
# print(boxes, v)
print(v)

# print(calc_v([Decimal(6), Decimal(8), Decimal(6)]))