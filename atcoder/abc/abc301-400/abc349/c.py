s = input()
t = input()
if t[-1] == "X":
    t = t[:-1]
s = s.upper()

idx = 0
for si in s:
    if si == t[idx]:
        idx += 1
        if idx == len(t):
            break

if idx == len(t):
    print("Yes")
else:
    print("No")