n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = [-1 for _ in range(n)]
big_a = a[:n // 2]
small_a = a[n // 2:]

for i in range(n):
    if i % 2 == 0:
        ans[i] = small_a[i // 2]
    else:
        ans[i] = big_a[i // 2]

# check
flag = True
for i in range(1, n - 1):
    if i % 2 == 1:
        if ans[i - 1] < ans[i] and ans[i] > ans[i + 1]:
            continue
        else:
            flag = False
            break
# print(ans)
print(['No', 'Yes'][flag])