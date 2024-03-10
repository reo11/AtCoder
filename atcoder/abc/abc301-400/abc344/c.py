n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

cands = set()

for ai in a:
    for bi in b:
        for ci in c:
            cands.add(ai + bi + ci)

ans = []
for xi in x:
    if xi in cands:
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep="\n")