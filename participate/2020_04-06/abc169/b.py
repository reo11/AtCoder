n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 1
for v in a:
    ans *= v
    if ans > 10**18:
        print(-1)
        exit()
print(ans)