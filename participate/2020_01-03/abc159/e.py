h, w, k = map(int, input().split())
s = [[i for i in list(map(int, list(input())))] for i in range(h)]


for i in range(2 ** (h-1)):
    choco = []
    div = 
    for j in range(h):
        if ((i >> j) & 1):
            choco.append(0)
        else:
            else: