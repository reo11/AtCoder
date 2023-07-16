n = int(input())
a = list(map(int, input().split()))

ans = [2, 0]
for k in range(2, 1001):
    count = 0
    for a_i in a:
        if a_i % k == 0:
            count += 1
    if count >= ans[1]:
        ans = [k, count]
print(ans[0])
