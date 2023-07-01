from typing import List, Union


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


if __name__ == "__main__":
    n = int(input())
    print(" ".join(map(str, sieve_of_eratosthenes(n, return_num=True))))
