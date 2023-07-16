def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


n = 10 ** 4
print(n)
a = []
num = 10 ** 6
idx = 0

while len(a) < n:
    n_ = num - idx
    if is_prime(n_):
        a.append(str(n_))
    idx += 1
    if n_ <= 0:
        print("error")
        break
print(" ".join(a))
