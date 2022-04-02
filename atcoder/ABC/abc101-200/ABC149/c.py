x = int(input())


def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


ans = x
while True:
    if is_prime(ans):
        break
    else:
        ans += 1
print(ans)
