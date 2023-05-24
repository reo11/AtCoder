t = int(input())
t_ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for j in range(n):
        if a[j] == 0:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    t_ans.append(ans)
print(*t_ans, sep="\n")