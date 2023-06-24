import sys
input = lambda: sys.stdin.readline().rstrip()

h_a, w_a = map(int, input().split())
a = []
for _ in [0]*h_a:
    a.append(list(input()))
h_b, w_b = map(int, input().split())
b = []
for _ in [0]*h_b:
    b.append(list(input()))
h_x, w_x = map(int, input().split())
x = []
for _ in [0]*h_x:
    x.append(list(input()))
x_sharp_count = 0

for x_i in range(h_x):
    for x_j in range(w_x):
        if x[x_i][x_j] == "#":
            x_sharp_count += 1

flag = False
# +-10まで全探索する
for a_i in range(0, 20):
    for a_j in range(0, 20):
        for b_i in range(0, 20):
            for b_j in range(0, 20):
                # AとBの処理
                # A
                c_sharp_count = 0
                iter_flag = True
                c = [["." for _ in range(30)] for _ in range(30)]
                for a_ii in range(h_a):
                    for a_jj in range(w_a):
                        if a[a_ii][a_jj] == "#":
                            c_sharp_count += 1
                            c[a_ii + a_i][a_jj + a_j] = "#"
                # B
                for b_ii in range(h_b):
                    for b_jj in range(w_b):
                        if b[b_ii][b_jj] == "#":
                            if c[b_ii + b_i][b_jj + b_j] != "#":
                                c_sharp_count += 1
                            c[b_ii + b_i][b_jj + b_j] = "#"

                for x_i in range(10, 10 + h_x):
                    for x_j in range(10, 10 + w_x):
                        if x[x_i - 10][x_j - 10] != c[x_i][x_j]:
                            iter_flag = False
                            break
                    if iter_flag == False:
                        break
                if iter_flag and c_sharp_count == x_sharp_count:
                    flag = True
                    break


if flag:
    print("Yes")
else:
    print("No")
