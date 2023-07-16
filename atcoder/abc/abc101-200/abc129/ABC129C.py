mod = 10 ** 9 + 7

n, m = map(int, input().split())
a = [1] * (n + 1)

for i in range(m):
    a[int(input())] = 0

l = [-1] * (n + 1)
l[n] = 1
l[n - 1] = a[n - 1]

num = n - 2
while num >= 0:
    if a[num] == 1:
        l[num] = (l[num + 1] + l[num + 2]) % mod
    else:
        l[num] = 0
    num -= 1

print(l[0])
