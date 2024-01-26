n = list(input())

flag = True
if len(n) == 1:
    flag = True
else:
    for i in range(len(n) - 1):
        if n[i] <= n[i + 1]:
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")
