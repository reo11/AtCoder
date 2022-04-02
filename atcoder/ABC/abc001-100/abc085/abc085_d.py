import math

n, h = map(int, input().split())

a = []
b = []
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

a_max = max(a)
b.sort(reverse=True)


idx = 0
count = 0
while h > 0:
    if idx < n and b[idx] > a_max:
        h -= b[idx]
        idx += 1
    else:
        count += math.ceil(h / a_max)
        break
    count += 1
print(count)
