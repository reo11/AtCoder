n = int(input())
cnt = 0
flag = False

for i in range(n):
    d = list(map(int, input().split()))
    if d[0] == d[1]:
        cnt += 1
    else:
        cnt = 0
    if cnt >= 3:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
