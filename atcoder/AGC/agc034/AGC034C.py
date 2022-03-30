import math
n, x = map(int, input().split())

blu =  [[0 for i in range(4)] for j in range(n)]
for i in range(n):
    blu[i][0], blu[i][1], blu[i][2]  = map(int, input().split())
    blu[i][3] = i
win_point_list = []

# uが大きい順にソート
blu_u = sorted(blu,  key=lambda x: x[2], reverse=True)
# lが小さい順にソート
# blu_l = sorted(blu,  key=lambda x: x[1])

# 最大の+、最小の-をそれぞれ求め、その組み合わせで0を作る
# index, min_minus, max_plus, l, u, is_used
score_list = [[0 for i in range(6)] for j in range(n)]

for i in range(n):
    score_list[i][0] = i
    score_list[i][1] = blu_u[i][0] * blu_u[i][1]
    score_list[i][2] = (x - blu_u[i][0]) * blu_u[i][2]
    score_list[i][3] = blu_u[i][1]
    score_list[i][4] = blu_u[i][2]
    score_list[i][5] = blu_u[i][0]

# +が多い順にソート
# 上下から取っていく
score_list.sort(key=lambda x: x[2], reverse=True)

#
a_index = 0
b_index = n-1

a_point = 0
b_point = 0

cost = 0

while a_index <= b_index + 1:
    if b_point <= a_point:
        b_point += score_list[b_index][1]
        b_index -= 1
    if a_point < b_point:
        if b_point - a_point < score_list[a_index][2]:
            p = math.ceil((b_point - a_point) / score_list[a_index][4])
            a_point += p * score_list[a_index][4]
            if a_index == b_index:
                cost += score_list[a_index][5] + p
            else:
                cost += p
            a_index += 1
            break
        else:
            a_point += score_list[a_index][2]
            a_index += 1
            cost += x
print(cost)
# [print(score) for score in score_list]

# a_point = 0
# b_point = 0
# u_i, l_i = 0, 0
# while u_i < n and l_i < n:
#     while u_i < n and used_index[blu_u[u_i][3]]:
#         u_i += 1
#     while l_i < n and used_index[blu_u[l_i][3]]:
#         l_i += 1
#     a_point += x * blu_u[u_i][2]
#     used_index[blu_u[u_i][3]] = True
#     b_point += blu_l[l_i][0] * blu_l[l_i][1]
#     used_index[blu_l[l_i][3]] = True
#     m = max(a_point, b_point)
#     a_point -= m
#     b_point -= m





