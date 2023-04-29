from typing import List, Union
import math

def sieve_of_eratosthenes(
    n: int, return_num: bool = False
) -> Union[List[bool], List[int]]:
    # O(nlognlogn)
    is_prime_list = [True] * (n + 1)
    is_prime_list[0] = False
    is_prime_list[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime_list[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime_list[j] = False

    if return_num:
        num_list = []
        for i, is_prime in enumerate(is_prime_list):
            if is_prime:
                num_list.append(i)
        return num_list
    else:
        return is_prime_list

n = int(input())
sqrt_n = math.sqrt(n)
l = sieve_of_eratosthenes(math.floor(sqrt_n), True)
ac = []

for i in range(len(l)):
    a = l[i]
    for j in range(i + 1, len(l)):
        c = l[j]
        if a * c > sqrt_n:
            break
        ac.append([a * c, [a, c]])
ans = 0
set_l = set(l)
# print(ac)
# print(set_l)
for v, set_v in ac:
    a = set_v[0]
    c = set_v[1]
    for i in range(len(l)):
        b = l[i]
        if b <= a:
            continue
        if b >= c:
            break
        if v ** 2 * b > n:
            break
        # print(a, b, c, a ** 2 * b * c ** 2)
        ans += 1
print(ans)