n = int(input())
a = list(map(int, input().split()))
l = [2, 4, 5, 6, 8]
count = 0
for i in range(n):
    while True:
        if a[i] in l:
            a[i] -= 1
            count += 1
        else:
            break
print(count)


