n = int(input())
p = list(map(int, input().split()))
p_sort = sorted(p)
flag = False

for i in range(n):
    for j in range(n):
        p_tmp = p[:]
        tmp = p_tmp[i]
        p_tmp[i] = p_tmp[j]
        p_tmp[j] = tmp
        match = True
        for k in range(n):
            if p_tmp[k] != p_sort[k]:
                match = False
        if match:
            flag = True
            break
    if flag:
        break

if flag:
    print("YES")
else:
    print("NO")