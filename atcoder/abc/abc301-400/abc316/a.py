n, h, x = map(int, input().split())
p = list(map(int, input().split()))

for i in range(n):
    if p[i] + h >= x:
        print(i + 1)
        exit()
