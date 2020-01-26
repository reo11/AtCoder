t = int(input())
for i in range(t):
    a, b, c, n = map(int, input().split())

    tmp = (3 * max(a, b, c)) - (a + b + c)
    if (n - tmp) % 3 == 0 and n - tmp >= 0:
        print("YES")
    else:
        print("NO")
