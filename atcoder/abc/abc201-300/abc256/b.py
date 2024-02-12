from collections import deque
n = int(input())
a = list(map(int, input().split()))

count = 0
while count < 3 and len(a) > 0:
    if count + a[-1] <= 3:
        ai = a.pop()
        count += ai
    else:
        break
print(len(a))
