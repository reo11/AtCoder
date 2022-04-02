n = int(input())


def wa(a, n, d):
    return (n * (2 * a + (n - 1) * d)) // 2


ans = 0
for i in range(1, n + 1):
    last = n - (n % i)
    num = (last - i) // i + 1
    ans += wa(i, num, i)
print(ans)
