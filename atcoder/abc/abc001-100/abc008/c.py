N = int(input())
C = [int(input()) for _ in range(N)]

ans = 0

for c in C:
    count = -1
    for i in C:
        if c % i == 0:
            count += 1
    if count % 2 == 0:
        ans += (count / 2 + 1) / (count + 1)
    else:
        ans += 1 / 2

print(ans)
