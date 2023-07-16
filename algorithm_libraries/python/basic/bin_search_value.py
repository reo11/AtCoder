from typing import Callable, Generator, Tuple


def bin_search_value(
    range_min: int, range_max: int, f: Callable[[int], bool]
) -> Generator[Tuple[int, int], None, None]:
    """
    f(x)が真になる最大のxと偽になる最小のxを求める
    Args:
        range_min (int): 最小値
        range_max (int): 最大値
    Returns:
        int: _description_
    """
    left = range_min - 1
    right = range_max + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if f(mid):
            right = mid
        else:
            left = mid
    return left, right


if __name__ == "__main__":

    def f(x: int) -> bool:
        return x > 10

    a, b = map(int, input().split())
    l, r = bin_search_value(a, b, f)
    print(f"{l} {r}")
