n = int(input())
t = [0] * n
for i in range(n):
    t[i] = int(input())
ans = 10**10
for i in range(2**n):
    a1 = 0
    a2 = 0
    for bit in range(n):
        if i & 2**bit > 0:
            a1 += t[bit]
        else:
            a2 += t[bit]
    ans = min(max(a1, a2), ans)
print(ans)
