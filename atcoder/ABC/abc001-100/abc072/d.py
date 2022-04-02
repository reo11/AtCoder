n = int(input())
p = list(map(int, input().split()))

i = 0
cnt = 0
while i < n:
    if i != n - 1:
        if p[i] == i + 1:
            tmp = p[i + 1]
            p[i + 1] = p[i]
            p[i] = tmp
            cnt += 1
    else:
        if p[i] == i + 1:
            tmp = p[i - 1]
            p[i - 1] = p[i]
            p[i] = tmp
            cnt += 1
    i += 1
print(cnt)
