n = int(input())
k = int(input())

min_ans = 10**10
for i in range(2 ** n):
    ans = 1
    for j in range(n):
        if i & 2 ** j:
            ans += k
        else:
            ans *= 2
    min_ans = min(min_ans, ans)
print(min_ans)

