n = int(input())
d = [[i for i in map(int, input().split())] for i in range(n)]
q = int(input())
p = [int(input()) for _ in range(q)]

t = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for i_ in range(i, n):
            for j_ in range(j, n):
                t[i][j] += d[i_][j_]

scores = [0 for _ in range(n*n+1)]

for i in range(n):
    for j in range(n):
        for i_ in range(i, n):
            for j_ in range(j, n):
                area = (i_ - i + 1) * (j_ - j + 1)
                score = t[i][j]
                if i_ + 1 < n:
                    score -= t[i_+1][j]
                if j_ + 1 < n:
                    score -= t[i][j_+1]
                if i_ + 1 < n and j_ + 1 < n:
                    score += t[i_+1][j_+1]

                scores[area] = max(scores[area], score)

m = 0
for i in range(len(scores)):
    m = max(scores[i], m)
    scores[i] = m

ans = 0
for i in range(q):
    print(scores[p[i]])