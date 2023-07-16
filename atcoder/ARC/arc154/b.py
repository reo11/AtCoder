from collections import defaultdict, deque

n = int(input())
s = list(input())
t = list(input())

count_s = defaultdict(int)
count_t = defaultdict(int)

for s_i in s:
    count_s[s_i] += 1
for t_i in t:
    count_t[t_i] += 1

flag = True
for i in range(26):
    c = chr(ord("a") + i)
    if count_s[c] != count_t[c]:
        flag = False
        break

if not flag:
    print(-1)
    exit()

ans = 0
s = deque(s)
t = deque(t)

# sの末尾とtの末尾から埋めていく
s_num = n - 1
t_num = n - 1
while s_num >= 0 and t_num >= 0:
    if s[s_num] == t[t_num]:
        s_num -= 1
        t_num -= 1
    else:
        t_num -= 1
print(s_num + 1)
