p = 1000000007
n = int(input())
A = list(map(int, input().split()))

ans = 1
cnt = [3 if i == 0 else 0 for i in range(n+1)]

for a in A:
    ans *= cnt[a]
    ans %= p
    cnt[a] -= 1
    cnt[a+1] += 1
print(ans)