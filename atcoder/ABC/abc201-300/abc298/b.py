import numpy as np

n = int(input())
a = []
for _ in range(n):
    a_i = np.array(list(map(int, input().split())))
    a.append(a_i)
a = np.array(a)
b = []
for _ in range(n):
    b_i = np.array(list(map(int, input().split())))
    b.append(b_i)
b = np.array(b)


def check(a, b):
    flag = True
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0:
                if b[i][j] == 0:
                    flag = False
    return flag

flag = False
for i in range(4):
    if check(a, b):
        flag = True
    a = np.rot90(a, -1)

if flag:
    print("Yes")
else:
    print("No")