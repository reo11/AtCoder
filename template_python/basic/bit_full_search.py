from typing import Iterator, List


def bit_full_search(max_bit: int) -> Iterator[List[int]]:
    for i in range(2 ** max_bit):
        bit_list = [0 for _ in range(max_bit)]
        for j in range(max_bit):
            if i & (2 ** j) > 0:
                bit_list[max_bit - j - 1] = 1
        yield bit_list
