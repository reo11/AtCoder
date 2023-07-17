n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))

ans = []
for i in range(n):
    cnt = 1
    num = i
    while i != a[num]:
        num = a[num]
        cnt += 1
    ans.append(cnt)
print(" ".join(list(map(str, ans))))
