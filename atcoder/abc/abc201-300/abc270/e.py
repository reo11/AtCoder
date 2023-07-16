from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

dq = deque()

a_list = []
for i, a_i in enumerate(a):
    a_list.append([a_i, i])
a_list = sorted(a_list)

for a_i, i in a_list:
    dq.append([a_i, i])

answers = []
count = 0
sum_c = 0
# 先頭から探索
while sum_c < k:
    while (dq[0][0] - count) == 0:
        a_pair = dq[0]
        answers.append([a_pair[1], 0])
        dq.popleft()

    if sum_c + ((dq[0][0] - count) * len(dq)) < k:
        count = dq[0][0]
        # sum_c -=
    else:
        dq_list = sorted(dq, key=lambda x: x[1])
