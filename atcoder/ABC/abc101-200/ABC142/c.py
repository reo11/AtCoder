n = int(input())
a = list(map(int, input().split()))
l = []

for i, a_ in enumerate(a):
    l.append([a_, i + 1])
l.sort()

ans = []
for i in range(len(l)):
    ans.append(str(l[i][1]))

print(" ".join(ans))
