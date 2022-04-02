n, y = map(int, input().split())

ans = "-1 -1 -1"

for man in range(n + 1):
    for go in range(n - man + 1):
        sen = n - (man + go)
        if man * 10000 + go * 5000 + sen * 1000 == y:
            ans = "{} {} {}".format(man, go, sen)
print(ans)
