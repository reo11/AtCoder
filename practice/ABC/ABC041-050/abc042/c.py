n, k = map(int, input().split())
d = list(map(str, input().split()))
num = [0 for _ in range(10)]

for v in d:
    num[int(v)] = 1

for j in range(10 * n):
    v = n + j
    v_l = list(str(v))
    flag = True
    for i in v_l:
        if num[int(i)] == 1:
            flag = False
            break
    if flag:
        print(v)
        exit()
