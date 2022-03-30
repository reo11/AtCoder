from collections import deque
import bisect
s = str(input())
t = str(input())

sc = [0] * 26
tc = [0] * 26

for i in range(len(s)):
    sc[ord(s[i]) - ord("a")] += 1
for i in range(len(t)):
    tc[ord(t[i]) - ord("a")] += 1

# 不可能な場合
for i in range(26):
    if tc[i] > 0 and sc[i] == 0:
        print(-1)
        exit()


alph = [[] for _ in range(26)]
for i in range(len(s)):
    alph[ord(s[i]) - ord("a")].append(i)

ans = [0] * len(t)
pre_num = -1
for i in range(len(t)):
    num = ord(t[i]) - ord("a")
    if i > 0:
        idx = bisect.bisect_right(alph[num], pre_num)
        if idx >= len(alph[num]):
            num_idx = alph[num][0]
        else:
            num_idx = alph[num][idx]
    else:
        num_idx = alph[num][0]
    ans[i] = num_idx
    pre_num = num_idx

count = 0
pre = -1
for v in ans:
    if pre >= v:
        count += 1
    pre = v

print(count * len(s) + ans[-1] + 1)