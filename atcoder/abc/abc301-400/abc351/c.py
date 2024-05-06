from collections import deque
n = int(input())
a = list(map(int, input().split()))

# 右方向から走査と左方向から走査を一回ずつ
a = deque(a)
tmp_a = deque()

while a:
    a_head = a.popleft()
    if len(tmp_a) > 0 and tmp_a[-1] == a_head:
        a_head += 1
        tmp_a.pop()
        a.appendleft(a_head)
        continue
    elif len(a) == 0:
        tmp_a.append(a_head)
        break
    else:
        if a[0] == a_head:
            a.popleft()
            a_head += 1
            a.appendleft(a_head)
        else:
            tmp_a.append(a_head)

a = tmp_a
tmp_a = deque()

while a:
    a_tail = a.pop()
    if len(tmp_a) > 0 and tmp_a[0] == a_tail:
        a_tail += 1
        tmp_a.popleft()
        a.append(a_tail)
        continue
    elif len(a) == 0:
        tmp_a.appendleft(a_tail)
        break
    else:
        if a[-1] == a_tail:
            a.pop()
            a_tail += 1
            a.append(a_tail)
        else:
            tmp_a.appendleft(a_tail)

print(len(tmp_a))
