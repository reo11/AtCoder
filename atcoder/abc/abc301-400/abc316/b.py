n = int(input())
a = list(map(int, input().split()))
a.sort()
min_a = min(a)
a = set(a)

for i in range(min_a, min_a + (n + 2)):
    if i not in a:
        print(i)
        exit()
