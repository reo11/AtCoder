from collections import defaultdict, deque
from typing import List, Union

n, p = map(int, input().split())


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


l = sieve_of_eratosthenes(p, True)


def make_combination(l):
    result = [1]
    for v in l:
        current_result_length = len(result)
        vv = v
        while vv <= n:
            for j in range(current_result_length):
                if vv * result[j] <= n:
                    result.append(vv * result[j])
                else:
                    break
            vv *= v
        result.sort()
    return result


# 半分全列挙
l_list = l[: len(l) // 3]
r_list = l[len(l) // 3 :]
all_l = sorted(make_combination(l_list))
all_r = sorted(make_combination(r_list))

ans = 0
for v in all_l:
    # 二分探索
    l = 0
    r = len(all_r)
    mid = 0
    while r - l > 1:
        mid = (l + r) // 2
        if v * all_r[mid] <= n:
            l = mid
        else:
            r = mid
    # print(mid)
    if v * all_r[mid] <= n:
        ans += mid + 1
    else:
        ans += mid
# print(all_l, all_r)
# print(len(all_l), len(all_r))
print(ans)
