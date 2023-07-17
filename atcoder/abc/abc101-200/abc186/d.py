def base10int(num_10, n):
    str_n = []
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n.append(num_10 % n)
        num_10 //= n
    return str_n[::-1]


n = int(input())

ans = 0
for i in range(1, n + 1):
    if not "7" in str(i) and not "7" in base10int(8, i):
        ans += 1
print(ans)
