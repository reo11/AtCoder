a, b, c = map(int, input().split())

flag1 = False
flag2 = False

if a + b == c:
    flag1 = True
if a - b == c:
    flag2 = True

if flag1 and flag2:
    print("?")
elif flag1:
    print("+")
elif flag2:
    print("-")
else:
    print("!")
