n = int(input())
xc = [input().split() for _ in range(n)]
xc = [(int(x[0]), str(x[1])) for x in xc]

red = list(filter(lambda x: x[1] == "R", xc))
blue = list(filter(lambda x: x[1] == "B", xc))
ans = []
red.sort()
blue.sort()
for v, c in red:
    ans.append(str(v))
for v, c in blue:
    ans.append(str(v))
print("\n".join(ans))
