MAX = 1000001

mod = 1000000007

prime = [0 for i in range(MAX)]

max_map = dict()

# function to return a^n

def power(a, n):

    if n == 0:
        return 1
    p = power(a, n // 2) % mod
    p = (p * p) % mod

    if n & 1:
        p = (p * a) % mod
    return p

# function to find the smallest prime
# factors of numbers upto MAX


def sieve():
    prime[0], prime[1] = 1, 1
    for i in range(2, MAX):
        if prime[i] == 0:
            for j in range(i * 2, MAX, i):
                if prime[j] == 0:
                    prime[j] = i
            prime[i] = i

# function to return the LCM modulo M


def lcmModuloM(arr, n):

    for i in range(n):
        num = arr[i]

        temp = dict()

        # temp stores mapping of prime factors
        # to its power for the current element
        while num > 1:

            # factor is the smallest prime
            # factor of num
            factor = prime[num]

            # Increase count of factor in temp
            if factor in temp.keys():
                temp[factor] += 1
            else:
                temp[factor] = 1

            # Reduce num by its prime factor
            num = num // factor

        for i in temp:
            # store the higest power of every prime
            # found till now in a new map max_map
            if i in max_map.keys():
                max_map[i] = max(max_map[i], temp[i])
            else:
                max_map[i] = temp[i]

    ans = 1

    for i in max_map:

        # LCM is product of primes to their
        # higest powers modulo M
        ans = (ans * power(i, max_map[i])) % mod
    return ans


def rep_sqr(base, k, mod):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return (rep_sqr(base, k / 2, mod) ** 2) % mod
    else:
        return (rep_sqr(base, k - 1, mod) * base) % mod

# a^(-1) == a^(m-2)


def flt(a, mod):
    return rep_sqr(a, mod-2, mod)

# Driver code
sieve()

# python > pypy
MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

lcm_ = lcmModuloM(a, n)

b = list(map(lambda x: lcm_ * flt(x, mod), a))
ans = 0
for i in range(len(b)):
    ans += b[i]
    ans %= MOD
print(ans)
