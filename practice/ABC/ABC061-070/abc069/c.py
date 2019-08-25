n = int(input())
a = list(map(int, input().split()))
count = [0] * 3
for i in range(n):
    if a[i] % 4 == 0:
        count[2] += 1
    elif a[i] % 2 == 0:
        count[1] += 1
    else:
        count[0] += 1

ans = False

if count[0] + (count[1] % 2) <= count[2] + 1:
    ans = True

if ans:
    print("Yes")
else:
    print("No")
