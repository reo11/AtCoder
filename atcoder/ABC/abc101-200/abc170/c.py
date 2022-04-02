x, n = map(int, input().split())
p = set(map(int, input().split()))

if x not in p:
    print(x)
    exit()

for i in range(1, 200):
    if x - i not in p:
        print(x - i)
        exit()
    elif x + i not in p:
        print(x + i)
        exit()
