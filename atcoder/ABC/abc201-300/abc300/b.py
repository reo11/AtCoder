import numpy as np
h, w = map(int, input().split())
a = []
b = []
for i in range(h):
    a.append(np.array(list(input())))
for i in range(h):
    b.append(np.array(list(input())))
a = np.array(a)
b = np.array(b)


# シフトi, jを全探索
ans = False
for i in range(h):
    for j in range(w):
        if np.roll(np.roll(a, i, axis=0), j, axis=1).tolist() == b.tolist():
            ans = True
if ans:
    print("Yes")
else:
    print("No")