n = int(input())
a = list(map(int, input().split()))

f = True
for v in a:
    if v % 2 == 0:
        if v % 3 == 0 or v % 5 == 0:
            pass
        else:
            f = False

if f:
    print('APPROVED')
else:
    print('DENIED')