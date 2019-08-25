n = int(input())

c = []
s = []
f = []

for i in range(n-1):
    c_, s_, f_ = map(int, input().split())
    c.append(c_)
    s.append(s_)
    f.append(f_)

for i in range(n-1):
    time = 0
    for j in range(i, n-1):
        if  time < s[j]:
            time = s[j]
        elif time % f[j] == 0:
            pass
        else:
            time += f[j] - (time % f[j])
        time += c[j]
    print(time)
print(0)