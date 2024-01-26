n = int(input())
a = list(map(int, input().split()))

me = a[0]
if n == 1:
    print(0)
elif max(a[1:]) > me:
    print(max(a[1:]) + 1 - me)
elif max(a[1:]) == me:
    print(1)
else:
    print(0)
