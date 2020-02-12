from collections import deque, defaultdict

t = int(input())
for i in range(t):
    s = list(str(input().rstrip()))
    deq = deque()
    d = defaultdict(int)

    cur = 0
    flag = True
    for c in s:
        if d[c] == 0:
            if cur == 0:
                deq.appendleft(c)
            elif cur == len(deq) - 1:
                deq.append(c)
                cur = len(deq) - 1
            else:
                flag = False
                break
            d[c] = 1
        else:
            if cur == len(deq) - 1:
                if deq[cur-1] == c:
                    cur -= 1
                else:
                    flag = False
                    break
            elif cur == 0:
                if deq[cur+1] == c:
                    cur += 1
                else:
                    flag = False
                    break
            else:
                if deq[cur+1] == c:
                    cur += 1
                elif deq[cur-1] == c:
                    cur -= 1
                else:
                    flag = False
                    break

    for alph in list('abcdefghijklmnopqrstuvwxyz'):
        if d[alph] == 0:
            deq.append(alph)

    if not flag:
        print("NO")
    else:
        print("YES")
        print("".join(list(map(str, deq))))