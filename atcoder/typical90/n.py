n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = 0
for a_i, b_i in zip(a, b):
    ans += abs(a_i - b_i)
print(ans)
