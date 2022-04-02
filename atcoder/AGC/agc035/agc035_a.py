n = int(input())
a = list(map(int, input().split()))
a.append(a[0])
a.insert(0, a[-2])

ans = 0

for i in range(n):
    ans ^= a[i]

if ans == 0:
    print("Yes")
else:
    print("No")
