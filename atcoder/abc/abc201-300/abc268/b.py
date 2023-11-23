s = list(input())
t = list(input())

if len(s) > len(t):
    print("No")
    exit()

flag = True
for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")