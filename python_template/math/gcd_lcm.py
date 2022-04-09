from functools import reduce
from typing import List


def gcd(a: int, b: int) -> int:
    # 最大公約数
    # (12, 18) -> 6
    while b:
        a, b = b, a % b
    return a

def gcd_list(numbers: List[int]) -> int:
    # 与えられた全ての数字の最大公約数
    return reduce(gcd, numbers)


def lcm(x: int, y: int) -> int:
    # 最小公倍数
    # (12, 18) -> 36
    return (x * y) // gcd(x, y)


def lcm_list(numbers: List[int]) -> int:
    # 与えられた全ての数字の最小公倍数
    return reduce(lcm, numbers)
