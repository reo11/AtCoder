a = list(map(int, input().split()))

ans = 0
for i, a_i in enumerate(a):
    ans += 2**i * a_i
print(ans)