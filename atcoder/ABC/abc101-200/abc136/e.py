from math import ceil


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


n, k = map(int, input().split())
a = list(map(int, input().split()))

a_sum = sum(a)

if a_sum - max(a) <= k:
    print(a_sum)

else:
    l = make_divisors(sum(a))
    m = len(l)
    ans = 1

    for gcd in l:
        mod = 0
        k_s = 0
        for a_ in a:
            mod_ = a_ % gcd
            if mod_ <= gcd - mod_:
                k_s += mod_
                mod += mod_
            else:
                k_s += gcd - mod_
                mod -= gcd - mod_

        if int(k_s / 2) + 1 < k and mod == 0:
            ans = max(ans, gcd)

    print(ans)
