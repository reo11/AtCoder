n = int(input())
s = list(input())

flag = False
ans = False
for i in range(n):
    if s[i] == "|":
        if flag:
            flag = False
        else:
            flag = True
    elif s[i] == "*" and flag:
        ans = True
if ans:
    print("in")
else:
    print("out")
