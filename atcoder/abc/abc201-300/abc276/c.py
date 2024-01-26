from collections import deque

n = int(input())
p = deque(list(map(int, input().split())))

candidate = deque([])

flag = True
ans = []
while p:
    num = p.pop()
    if flag == False:
        ans.append(num)
        continue
    elif len(candidate) == 0 or candidate[-1] > num:
        candidate.append(num)
    else:
        # numより小さい最大の値を前に出す
        # その後numを含め降順に並べる
        max_num = 0
        for c in candidate:
            if c < num:
                max_num = max(max_num, c)
        for c in candidate:
            if c == max_num:
                continue
            ans.append(c)
        ans.append(num)
        ans = sorted(ans)
        ans.append(max_num)
        flag = False
ans = reversed(ans)
print(*ans, sep=" ")
