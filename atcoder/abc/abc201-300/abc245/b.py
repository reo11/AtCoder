n = int(input())
a = set(map(int, input().split()))

for i in range(2001):
    if i in a:
        continue
    else:
        print(i)
        break
