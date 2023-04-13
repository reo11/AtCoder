import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush

input = sys.stdin.readline

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(q)]

meibo = defaultdict(int)
exsists = defaultdict(lambda: set())
groups = defaultdict(lambda: [])
all_groups = []

for i in range(n):
    a, b = ab[i]
    heappush(groups[b], [-a, i + 1])
    exsists[b].add(i + 1)
    meibo[i + 1] = b

for group_id in groups.keys():
    max_rate, max_rate_id = heappop(groups[group_id])
    heappush(groups[group_id], [max_rate, max_rate_id])
    heappush(all_groups, [-max_rate, group_id, max_rate_id])

ans = []
for i in range(q):
    print(f"\n\nRound{i + 1}")
    c, d = cd[i]
    exsists[d].add(c)
    exsists[meibo[c]].discard(c)
    heappush(groups[d], [-ab[c - 1][0], c])
    meibo[c] = d

    while True:
        delete_group_flag = False
        min_rate, group_id, person_id = heappop(all_groups)
        max_rate, max_rate_id = heappop(groups[group_id])
        if person_id == max_rate_id and person_id in exsists[group_id]:
            heappush(groups[group_id], [max_rate, max_rate_id])
            heappush(all_groups, [-max_rate, group_id, max_rate_id])
            break
            # 最新情報でない場合は正しい情報に更新
            # step1. グループ内の最大レートの存在確認
            # step2. その情報を全体に対して適用
        else:
            while max_rate_id not in exsists[group_id]:
                if len(groups[group_id]) == 0:
                    groups.pop(group_id)
                    delete_group_flag = True
                    break
                max_rate, max_rate_id = heappop(groups[group_id])
            if not delete_group_flag:
                heappush(groups[group_id], [max_rate, max_rate_id])
                heappush(all_groups, [-max_rate, group_id, max_rate_id])
    min_rate, group_id, person_id = heappop(all_groups)
    heappush(all_groups, [min_rate, group_id, person_id])
    ans.append(min_rate)
    print(groups)
    print(all_groups)
    print(exsists)
    print(meibo)
print(ans)
