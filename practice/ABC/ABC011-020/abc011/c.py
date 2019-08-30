n = int(input())
ng = [int(input()) for _ in range(3)]
if n in ng:
    print("NO")
    exit()
for i in range(100):
    if n == 0:
        break
    for i in range(1, 4)[::-1]:
        if i == 1:
            if n - i in ng or n - i < 0:
                print("NO")
                exit()
            else:
                n -= i
                break
        else:
            if n - i in ng or n - i < 0:
                continue
            else:
                n -= i
                break
if n == 0:
    print("YES")
else:
    print("NO")