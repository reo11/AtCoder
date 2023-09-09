import decimal
from collections import defaultdict
from itertools import permutations
c = [list(map(int, input().split())) for _ in range(3)]
c_list = [c[0][0], c[0][1], c[0][2], c[1][0], c[1][1], c[1][2], c[2][0], c[2][1], c[2][2]]

# 順列全探索
count_all = 0
count_ok = 0
naname_group = {
    0: [0],
    2: [1],
    4: [0, 1],
    6: [1],
    8: [0]
}
for perm in permutations(list(range(9))):
    # print(perm)
    tate = defaultdict(lambda: set())
    yoko = defaultdict(lambda: set())
    naname = defaultdict(lambda: set())
    flag = True
    count_all += 1
    for i in perm:
        ci = c_list[i]
        if ci in tate[i // 3] and len(tate[i // 3]) == 1:
            flag = False
            break
        else:
            tate[i // 3].add(ci)
        if ci in yoko[i % 3] and len(yoko[i % 3]) == 1:
            flag = False
            break
        else:
            yoko[i % 3].add(ci)
        if i in naname_group:
            for groupi in naname_group[i]:
                if ci in naname[groupi] and len(naname[groupi]) == 1:
                    flag = False
                    break
                else:
                    naname[groupi].add(ci)
            if not flag:
                break
    if flag:
        count_ok += 1
# print(count_all, count_ok)
print(decimal.Decimal(count_ok) / decimal.Decimal(count_all))