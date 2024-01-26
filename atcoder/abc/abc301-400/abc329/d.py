MAX_N = 200001
import heapq
from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))


def calc_value(person_num, value):
    # 同着の場合に若い番号を優先する
    return value * MAX_N + (MAX_N - person_num)


queue = []
heapq.heapify(queue)

counter = defaultdict(int)

ans = []

for i in range(m):
    ai = a[i]
    counter[ai] += 1
    heapq.heappush(queue, (-calc_value(ai, counter[ai]), ai))
    ans.append(queue[0][1])

print(*ans, sep="\n")
