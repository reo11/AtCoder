n = int(input())
max_dis = 0


def dis(v1, v2):
    return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** 0.5


pos_list = []
for _ in range(n):
    x, y = map(int, input().split())
    pos_list.append((x, y))
for v1 in pos_list:
    for v2 in pos_list:
        max_dis = max(max_dis, dis(v1, v2))
print(max_dis)
