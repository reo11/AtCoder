import time


def power_func_while(a: int, b: int, mod: int) -> int:
    ans = 1
    while b > 0:
        if b & 1:
            ans = ans * a % mod
        a = a * a % mod
        b >>= 1
    return ans


def power_func_rec(a: int, b: int, mod: int) -> int:  # type: ignore
    if b == 0:
        return 1
    if b % 2 == 0:
        d = power_func_rec(a, b // 2, mod)
        return d * d % mod
    if b % 2 == 1:
        return (a * power_func_rec(a, b - 1, mod)) % mod


MOD = 10 ** 9 + 7
start = time.time()
for _ in range(10 ** 5):
    n = 10 ** 5
    _ = power_func_rec(n, MOD - 2, MOD)
elapsed_time = time.time() - start
print("再帰:{0}".format(elapsed_time) + "[sec]")

start = time.time()
for _ in range(10 ** 5):
    n = 10 ** 5
    _ = power_func_while(n, MOD - 2, MOD)
elapsed_time = time.time() - start
print("while:{0}".format(elapsed_time) + "[sec]")
