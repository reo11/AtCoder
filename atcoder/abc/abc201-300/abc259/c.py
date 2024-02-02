from collections import deque
s = list(input())
t = list(input())

s = deque(s)
t = deque(t)
flag = True
while len(t) > 0:
    # tの文字が連続する限り取り出す
    t_head = t.popleft()
    count_t = [t_head, 1]
    while len(t) > 0 and t[0] == count_t[0]:
        t.popleft()
        count_t[1] += 1

    # sの文字がt_headに一致する限り取り出す
    count_s = 0
    while len(s) > 0 and s[0] == t_head:
        s.popleft()
        count_s += 1

    if count_s == 0:
        flag = False
        break
    elif count_s == 1 and count_t[1] > 1:
        flag = False
        break
    elif count_s > count_t[1]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
