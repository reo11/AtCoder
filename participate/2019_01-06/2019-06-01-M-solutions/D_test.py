from collections import defaultdict
connection = defaultdict(lambda: [])

n = int(input())

ab = []
for i in range(n-1):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)
    ab.append((a, b))

l = []
for i in range(1, n+1):
    l.append([i, len(connection[i])])

l.sort(key=lambda x: x[1], reverse=True)

c = list(map(int, input().split()))
c.sort(reverse=True)

ans = [0] * (n+1)
for i in range(n):
    ans[l[i][0]] = c[i]


score = 0
for a, b in ab:
    score += min(ans[a], ans[b])

print(score)
print(" ".join(map(str, c)))
