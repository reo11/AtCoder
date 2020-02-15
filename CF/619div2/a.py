t = int(input())
for i in range(t):
    a = str(input().rstrip())
    b = str(input().rstrip())
    c = str(input().rstrip())

    flag = True
    for i in range(len(a)):
        if len(set([a[i], b[i], c[i]])) == 3:
            flag = False
            break
        if a[i] == b[i] and a[i] != c[i]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")