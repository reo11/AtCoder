k = int(input())
n = 50

ans = list(map(lambda x: x + (k // n), range(n)))

for i in range(k % n):
    for j in range(n):
        if i == j:
            ans[j] += n
        else:
            ans[j] -= 1
print(n)
print(" ".join(list(map(str, ans))))