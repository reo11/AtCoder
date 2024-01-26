h, w = map(int, input().split())
s_tmp = [list(input()) for _ in range(h)]
t_tmp = [list(input()) for _ in range(h)]

s = []
for i in range(w):
    s.append([])
    for j in range(h):
        s[-1].append(s_tmp[j][i])
t = []
for i in range(w):
    t.append([])
    for j in range(h):
        t[-1].append(t_tmp[j][i])
for i in range(w):
    s[i] = "".join(s[i])
    t[i] = "".join(t[i])
s.sort()
t.sort()

flag = True
for i in range(w):
    if s[i] != t[i]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
