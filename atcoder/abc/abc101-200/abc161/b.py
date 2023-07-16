n, m = map(int, input().split())
a = list(map(int, input().split()))
s_a = sum(a)
a = list(filter(lambda x: x >= 1 / (4 * m) * s_a, a))
if len(a) >= m:
    print("Yes")
else:
    print("No")
