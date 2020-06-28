n = int(input())
h = list(map(int, input().split()))

v = 1
flag = True
for i in range(n):
    if v < h[i]:
        v = h[i] - 1
    elif v == h[i]:
        pass
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
