t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    flag = True
    count_odd = 0

    for v in a:
        if v % 2 == 1:
            count_odd += 1
    count_even = n - count_odd
    if count_even == 0 and n % 2 == 0:
        flag = False
    if count_odd == 0:
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")