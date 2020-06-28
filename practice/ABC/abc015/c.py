n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

def dfs(num, l):
    global t, n, k

    if num == n:
        xor = 0
        for v in l:
            xor ^= v
        if xor == 0:
            print("Found")
            exit()
        return
    for i in range(k):
        dfs(num+1, l[:] + [t[num][i]])

dfs(0, [])
print("Nothing")