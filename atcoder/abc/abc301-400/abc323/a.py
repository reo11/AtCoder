s = list(input())

flag = True
for i in range(1, 9):
    if i * 2 - 1 > len(s) - 1:
        break
    if s[i * 2 - 1] != "0":
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")