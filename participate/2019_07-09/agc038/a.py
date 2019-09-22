import numpy as np
h, w, a, b = map(int, input().split())

s = [[0 for _ in range(w)] for _ in range(h)]
s = np.array(s)

idx = 0
c_idx = 0
for i in range(h):
    for j in range(idx, idx + (w - a)):
        j %= w
        s[i][j] = 1
    idx += (w - a)
    idx %= w

for i in range(h):
    sum_ = np.sum(s[i])
    if not(min(sum_, w - sum_) == b):
        print("No")
        exit()

s = s.transpose()

for i in range(w):
    sum_ = np.sum(s[i])
    if not(min(sum_, h - sum_) == b):
        print("No")
        exit()

s = s.transpose()

ans = []
for i in range(h):
    for j in range(w):
        ans.append(str(s[i][j]))
    if i == h-1:
        break
    ans.append("\n")
print("".join(ans))

