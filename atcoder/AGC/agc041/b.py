import math

n, m, v, p = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# if v <= p:
#     for i in range(v-1):
#         a[n-i-1] = a[n-i-1] + m
#     boader = a[-p]
#     boader -= m

#     if boader <= 0:
#         print(n)
#     else:
#         count = 0
#         for i in range(n):
#             if a[i] >= boader:
#                 count += 1
#         print(count)
# else:
sum_ = sum(a)
for i in range(1, p + 1):
    sum_ -= a[n - i]
start = n - p - 1
count = p
print(a)
while True:
    sum_ -= a[start]
    if start == 0:
        break
    if a[start] + m >= math.ceil((m * (v - (p - 1)) + sum_) / start):
        count += 1
    else:
        break
    start -= 1
print(count)
