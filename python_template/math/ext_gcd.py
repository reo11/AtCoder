from typing import Tuple


def extgcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    else:
        d, y, x = extgcd(b, a % b)
        y -= a // b * x
        return d, x, y
