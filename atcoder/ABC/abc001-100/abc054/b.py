n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(input()))
for i in range(m):
    b.append(list(input()))


for s_h in range(n - m + 1):
    for s_w in range(n - m + 1):
        flag = True
        for i in range(m):
            for j in range(m):
                if a[s_h + i][s_w + j] != b[i][j]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print("Yes")
            break
    if flag:
        break
if not flag:
    print("No")
