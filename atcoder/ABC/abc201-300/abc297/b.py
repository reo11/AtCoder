s = input()

def check1(s):
    l = []
    for i in range(len(s)):
        if s[i] == "B":
            l.append(i)
    return l[0] % 2 != l[1] % 2

def check2(s):
    k = 0
    r = []
    for i in range(len(s)):
        if s[i] == "K":
            k = i
        if s[i] == "R":
            r.append(i)
    r.sort()
    return r[0] < k and k < r[1]

if check1(s) and check2(s):
    print("Yes")
else:
    print("No")