s = input()
if len(s) == 3:
    f = True
    for i in range(3):
        if s[i] not in list(map(str, range(0, 10))):
            f = False
    if f:
        print(int(s) * 2)
    else:
        print("error")
else:
    print("error")