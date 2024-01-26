from collections import defaultdict

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

# 縦横にカウンターを設置する
# 0個になったらdiscardする
counter = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
# l = []

for i in range(h):
    for j in range(w):
        cij = c[i][j]
        counter["h"][i][cij] += 1
        counter["w"][j][cij] += 1
deleted_c_count = defaultdict(lambda: defaultdict(lambda: 0))
count = 0
while True:
    discard_list = []
    # 行方向
    for hi in counter["h"].keys():
        if len(counter["h"][hi].keys()) == 1:
            for key in counter["h"][hi].keys():
                if counter["h"][hi][key] >= 2:
                    discard_list.append(["h", hi, key])
    # 列方向
    for wi in counter["w"].keys():
        if len(counter["w"][wi].keys()) == 1:
            for key in counter["w"][wi].keys():
                if counter["w"][wi][key] >= 2:
                    discard_list.append(["w", wi, key])

    if len(discard_list) == 0:
        break
    for s, idx, key_num in discard_list:
        if key_num in counter[s][idx]:
            counter[s].pop(idx)
            if s == "h":
                for i in counter["w"].keys():
                    if key_num in counter["w"][i]:
                        counter["w"][i][key_num] -= 1
                        if counter["w"][i][key_num] == 0:
                            counter["w"][i].pop(key_num)
            else:
                for i in counter["h"].keys():
                    if key_num in counter["h"][i]:
                        counter["h"][i][key_num] -= 1
                        if counter["h"][i][key_num] == 0:
                            counter["h"][i].pop(key_num)
    pre_discard_count = len(discard_list)
ans = 0
for s in ["h"]:
    for idx in counter[s].keys():
        for v in counter[s][idx].values():
            ans += v
print(ans)
