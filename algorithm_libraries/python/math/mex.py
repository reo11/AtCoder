from typing import List


def mex(array: List[int]) -> int:
    """Return mex of array
    Args:
        array (List[int]): list of int
    Returns:
        int: mex of array
    """
    array_set = set(array)
    n = len(array_set)
    for m in range(n + 1):
        if m in array_set:
            continue
        else:
            return m
    return n