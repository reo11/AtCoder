import numpy as np
n, k = map(int, input().split())
a = list(int(i) for i in input().split())

sum_l = np.cumsum(a)
sum_l = np.insert(sum_l, 0, 0)
# sum_r = np.cumsum(a[::-1])
# np.insert(sum_r, 0, 0)
# sum_r = sum_r[::-1]

l = 0
r = 1
m = 0
len_list = []
while l < n and r < n:
    if sum_l[r] - sum_l[l] < k:
        r += 1
    else:
        len_list.append(r - l + 1)
        m += 1
        l = r
        r = l + 1

print(len_list)
print(m)
print(sum_l)
# print(sum_r)
