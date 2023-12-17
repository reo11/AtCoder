import itertools
from collections import deque
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]

# Bは固定
def calc_cost(vector):
    cost = 0
    base_vector = deque(list(range(len(vector))))
    for v in vector:
        tmp = deque()
        while base_vector[0] != v:
            tmp.append(base_vector.popleft())
            cost += 1
        base_vector.popleft()
        for _ in range(len(tmp)):
            base_vector.appendleft(tmp.pop())
        # print(base_vector, cost)
    return cost

# 列の入れ替え全列挙
ans = -1
for cols in itertools.permutations(range(w)):
    for rows in itertools.permutations(range(h)):
        # Aの列を入れ替え
        AA = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                AA[i][j] = A[rows[i]][cols[j]]
        if AA == B:
            cost = calc_cost(cols) + calc_cost(rows)
            # print(AA, B, cols, rows, cost)
            if ans == -1:
                ans = cost
            else:
                ans = min(ans, cost)
print(ans)

