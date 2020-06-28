s = str(input())
n = int(input())

idx = 0
for c1 in list(s):
    for c2 in list(s):
        idx += 1
        if idx == n:
            print(c1 + c2)