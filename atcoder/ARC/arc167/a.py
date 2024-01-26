from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

b = []
a_que = deque(a)
# 末尾 n // 2個は単独で乗せる
# n // 2
for i in range(2 * m - n):
    b.append([a_que.pop()])

# 2こおくものは先頭と末尾を乗せる
size = m - len(b)
for i in range(size):
    b.append([a_que.pop(), a_que.popleft()])

ans = 0
for bi in b:
    ans += sum(bi) ** 2
# print(b)
print(ans)
