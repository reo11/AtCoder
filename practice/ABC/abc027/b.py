n = int(input())
a = list(map(int, input().split()))
v = sum(a) / n
if sum(a) % n == 0:
    count = 0
    for i in range(1, n):
        if sum(a[:i]) != i * v:
            count += 1
    print(count)

else:
    print(-1)
