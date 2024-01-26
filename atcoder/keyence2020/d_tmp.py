import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = []
for i in range(n):
    ab.append([a[i], b[i]])

# 後ろからチェック

i = n - 1
flag = False
count = 0
for _ in range(10**5):
    if i == 0:
        flag = True
        break
    if ab[i][0] < ab[i - 1][0]:
        if ab[i - 1][1] < ab[i - 2][1]:
            tmp = ab[i - 1]
            ab[i - 1] = [ab[i - 2][1], ab[i - 2][0]]
            ab[i - 2] = [tmp[1], tmp[0]]
            count += 1
        elif ab[i - 1][1] < ab[i][1]:
            tmp = ab[i]
            ab[i] = [ab[i - 1][1], ab[i - 1][0]]
            ab[i - 1] = [tmp[1], tmp[0]]
            count += 1
        else:
            break
        i = n - 1
    else:
        i -= 1
if flag:
    print(count)
else:
    print(-1)
