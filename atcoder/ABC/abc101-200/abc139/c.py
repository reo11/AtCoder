n = int(input())
h = list(map(int, input().split()))
max_ = 0

pre = -1
count = 0
for i in range(n):
    if pre >= h[i]:
        count += 1
    else:
        count = 0
    pre = h[i]
    max_ = max(max_, count)
print(max_)
