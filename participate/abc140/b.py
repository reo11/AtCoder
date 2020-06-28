n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

t = 0
pre = -1
for i in range(n):
    a_ = a[i] - 1
    t += b[a_]
    if i > 0 and a_ - 1 == pre:
        t += c[pre]
    pre = a_
print(t)
