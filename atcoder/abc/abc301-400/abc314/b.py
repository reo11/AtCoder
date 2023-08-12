n = int(input())
c = []
a = []
for _ in range(n):
    ci = int(input())
    ai = list(map(int, input().split()))
    c.append(ci)
    a.append(ai)
x = int(input())

ans = [10**9, []]
for i in range(n):
    if x in a[i]:
        if len(a[i]) < ans[0]:
            ans[0] = len(a[i])
            ans[1] = [i + 1]
        elif len(a[i]) == ans[0]:
            ans[1].append(i + 1)
out = sorted(ans[1])
print(len(out))
print(*out, sep=" ")