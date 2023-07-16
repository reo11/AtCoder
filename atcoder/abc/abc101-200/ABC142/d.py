def divisor(n):  # nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table


# a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


a, b = map(int, input().split())

a_div = divisor(a)
b_div = divisor(b)
ans = set(a_div) & set(b_div)

count = 0
for i in ans:
    if is_prime(i):
        count += 1

print(count + 1)
