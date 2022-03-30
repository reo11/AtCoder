h, n = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)

if h <= s:
    print("Yes")
else:
    print("No")