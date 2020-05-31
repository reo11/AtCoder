h, w = map(int, input().split())
s = [[i for i in input().split()] for i in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "snuke":
            print("{}{}".format(chr(ord("A") + j), i+1))