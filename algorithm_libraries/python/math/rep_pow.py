def rep_pow(a: int, k: int, p: int = 10**9 + 7) -> int:
    # calculate exponentiation: a^k mod p
    # O(log(p))
    ans = 1
    while k > 0:
        if k & 1:
            ans = ans * a % p
        a = a * a % p
        k >>= 1
    return ans


if __name__ == "__main__":
    n, m, p = map(int, input().split())
    print(rep_pow(n, m, p))
