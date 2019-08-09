n = int(input())
sp = []

for i in range(n):
    s, p = input().split()
    p = int(p)
    sp.append([p, s])
sp.sort(reverse=True)
sum_ = sum([x[0] for x in sp])
if sp[0][0] > sum_ // 2:
    print(sp[0][1])
else:
    print("atcoder")
