from collections import deque

k = int(input())
que = deque([i for i in range(1, 10)])
i = 0
while True:
    i += 1
    num = que.popleft()
    if i == k:
        print(num)
        exit()
    if num % 10 > 0:
        que.append(num * 10 + ((num % 10) - 1))
    que.append(num * 10 + (num % 10))
    if num % 10 < 9:
        que.append(num * 10 + ((num % 10) + 1))
