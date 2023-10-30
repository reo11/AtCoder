from collections import deque

n = input()

queue = deque([n])

while queue:
    num = queue.popleft()
    # print(num)
    if len(num) == 0:
        continue
    if int(num) % 3 == 0:
        print(len(n) - len(num))
        exit()
    for i in range(len(num)):
        next_num = num[:i] + num[i+1:]
        queue.append(next_num)

print(-1)