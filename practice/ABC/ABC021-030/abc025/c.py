B = [[int(i) for i in input().split()] for _ in range(2)]
C = [[int(i) for i in input().split()] for _ in range(3)]

p = [0] * 9
m = {}

def solve(t, a):
    if t == 9:
        s = 0
        for i in range(6):
            if p[i] == p[i + 3]:
                s += B[i // 3][i % 3]
        for i in (0, 1, 3, 4, 6, 7):
            if p[i] == p[i + 1]:
                s += C[i // 3][i % 3]
        return s

    if a and (a in m):
        return m[a]

    r, n = -10 ** 10, (-1 if t % 2 == 1 else 1)
    for i in range(9):
        if p[i] == 0:
            p[i] = n
            r = max(r, n * solve(t + 1, tuple(j for j in p)))
            p[i] = 0
    m[tuple(i for i in p)] = n * r
    return n * r

su = sum(map(sum, B)) + sum(map(sum, C))
ans = solve(0, None)
print(ans)
print(su - ans)
