n = int(input())
s = [[i for i in list(str(input()))] for i in range(n)]
for i in reversed(range(n-1)):
    for j in range(1, 2*n-2):
        if s[i][j] != '#':
            continue
        f = False
        if 0 <= j-1 <= 2*n-2:
            if s[i+1][j-1] == 'X':
                f = True
        if 0 <= j+1 <= 2*n-2:
            if s[i+1][j+1] == 'X':
                f = True
        if s[i+1][j] == 'X':
            f = True
        if f:
            s[i][j] = 'X'
for i in range(n):
    print("".join(s[i]))
