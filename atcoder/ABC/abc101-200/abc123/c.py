from math import ceil

n = int(input())
a = []
for i in range(5):
    a.append(int(input()))

ans = ceil(n / min(a)) + 4
print(ans)
