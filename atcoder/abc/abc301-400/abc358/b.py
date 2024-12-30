from collections import deque
n, a = map(int, input().split())
t = list(map(int, input().split()))
t = deque(t)

time = 0
wait_list = []
ans = []
while t or wait_list:
    while len(t) > 0 and time > t[0]:
        x = t.popleft()
        wait_list.append(x)
    if len(wait_list) == 0:
        x = t.popleft()
        wait_list.append(x)
        time = x

    wait_list.pop()
    time += a
    ans.append(time)
print(*ans, sep="\n")