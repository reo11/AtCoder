from typing import Iterator, List


def bit_full_search(max_bit: int) -> Iterator[List[int]]:
    """
    bit全探索
    2状態を持つmax_bit個の要素に対して、0/1の組み合わせを全探索する
    計算量はO(2^max_bit)
    Args:
        max_bit (int): 要素数
    Yields:
        Iterator[List[int]]: max_bitの長さの0/1の組み合わせ
    """
    for i in range(2**max_bit):
        bit_list = [0 for _ in range(max_bit)]
        for j in range(max_bit):
            if i & (2**j) > 0:
                bit_list[max_bit - j - 1] = 1
        yield bit_list
