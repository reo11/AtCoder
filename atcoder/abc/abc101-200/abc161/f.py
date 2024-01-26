from math import sqrt

n = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


# def solve1(n):
#     ans = []
#     for k in range(2, n+1):
#         tmp = n
#         while tmp % k == 0:
#             tmp = tmp // k
#             if tmp < k:
#                 break
#         tmp = tmp % k
#         if tmp == 1:
#             ans.append(k)
#     return ans, len(ans)


def solve2(n):
    div1 = make_divisors(n - 1)
    div2 = make_divisors(n)
    div = list(set(filter(lambda x: x > 1, div1 + div2)))
    ans = []
    for k in div:
        tmp = n
        while tmp % k == 0:
            tmp = tmp // k
            if tmp < k or tmp == 1:
                break
        tmp = tmp % k
        if tmp == 1:
            ans.append(k)
    return len(ans)


print(solve2(n))
