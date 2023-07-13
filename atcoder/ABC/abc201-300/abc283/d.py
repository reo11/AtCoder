from collections import deque
s = list("(" + input() + ")")
n = len(s)

q = deque()
box = set()
flag = True
for s_i in s:
    if s_i == "(":
        q.appendleft([])
    elif s_i == ")":
        balls = q.popleft()
        for ball in balls:
            box.discard(ball)
    else:
        if s_i in box:
            flag = False
            break
        balls = q.popleft()
        balls.append(s_i)
        q.appendleft(balls)
        box.add(s_i)

if flag:
    print("Yes")
else:
    print("No")