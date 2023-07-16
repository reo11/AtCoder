n = int(input())
a = list(map(int, input().split()))

ans = []
base = 0
for i in range(n):
    if i % 2 == 0:
        base += a[i]
    else:
        base -= a[i]
base //= 2

for i in range(n)[::-1]:
    base = a[i] - base
    ans.append(base)
ans = list(map(lambda x: str(x * 2), ans))
ans = ans[::-1]
print(" ".join(ans))
