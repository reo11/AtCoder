import heapq
import time

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    # 幅優先探索
    count = 0
    ans = 0
    already = set()
    q = a.copy()
    heapq.heapify(q)

    while count < k:
        if len(q) > 0:
            min_a = heapq.heappop(q)
        else:
            for a_i in a:
                heapq.heappush(q, min_a + a_i)
            continue

        if min_a in already:
            continue
        else:
            already.add(min_a)
        ans = min_a
        count += 1
        if count == k:
            break
        for a_i in a:
            heapq.heappush(q, min_a + a_i)
    return ans
print(solve())