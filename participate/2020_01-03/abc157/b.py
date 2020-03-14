a = [[i for i in list(map(int, input().split()))] for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

bingo = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(n):
            if b[k] == a[i][j]:
                bingo[i][j] = 1

f = False
for i in range(3):
    f_tmp = True
    for j in range(3):
        if not(bingo[i][j] and f_tmp):
            f_tmp = False
    if f_tmp:
        f = True

for j in range(3):
    f_tmp = True
    for i in range(3):
        if not(bingo[i][j] and f_tmp):
            f_tmp = False
    if f_tmp:
        f = True

f_tmp = True
for i in range(3):
    if not(bingo[i][i] and f_tmp):
        f_tmp = False
if f_tmp:
    f = True

f_tmp = True
for i in range(3):
    if not(bingo[2-i][i] and f_tmp):
        f_tmp = False
if f_tmp:
    f = True

if f:
    print('Yes')
else:
    print('No')
