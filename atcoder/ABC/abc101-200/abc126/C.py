import math
n, k = map(int, input().split())

def calc(dise, k):
    return (1/2) ** math.ceil(math.log2(k/dise))

ans = 0

for i in range(n):
    if i+1 >= k:
        ans += 1/n
    else:
        ans += calc(i+1, k) / n
print(ans)
# pypyだとRE...何故？