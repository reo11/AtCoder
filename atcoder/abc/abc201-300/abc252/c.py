n = int(input())
s = []

for i in range(n):
    si = list(map(int, list(input())))
    for _ in range(4):
        si = si + si
    s.append(si)

ans = float("inf")
for i in range(10):
    t = 0
    for j in range(n):
        while True:
            if s[j][t] == i:
                if j < n - 1:
                    t += 1
                break
            else:
                t += 1
    ans = min(ans, t)
print(ans)



