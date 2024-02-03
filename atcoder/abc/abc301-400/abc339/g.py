n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = []
for _ in range(q):
    alpha, beta, gamma = map(int, input().split())
    queries.append((alpha, beta, gamma))

def decode(alpha, beta, gamma, pre_b):
    l = alpha ^ pre_b
    r = beta ^ pre_b
    x = gamma ^ pre_b
    return l, r, x

ans = []
pre_b = 0
for query in queries:
    alpha, beta, gamma = query
    l, r, x = decode(alpha, beta, gamma, pre_b)
    ansi = 0
    for i in range(l - 1, r):
        if a[i] <= x:
            ansi += a[i]
    ans.append(ansi)
    pre_b = ansi
print(*ans, sep='\n')