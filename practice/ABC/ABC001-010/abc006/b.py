n = int(input())
a = [0] * (10 ** 6 + 1)
a[3] = 1
for i in range(4, 10 ** 6 + 1):
    a[i] = (a[i-1] + a[i-2] + a[i-3]) % 10007
print(a[n])