n = int(input())
a = list(map(int, input().split()))

a_base = a[0]
flag = True

for ai in a:
    if ai != a_base:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
