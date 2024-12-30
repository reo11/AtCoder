from typing import Iterator, List

n, m = map(int, input().split())
s = [input() for _ in range(n)]
popcorns = [set() for _ in range(n)]

for i, si in enumerate(s):
    for j in range(m):
        if si[j] == "o":
            popcorns[i].add(j)

# bit全探索
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

ans = n
for bit_list in bit_full_search(n):
    popcorn = set()
    bit_count = 0
    for i, bit in enumerate(bit_list):
        if bit == 1:
            bit_count += 1
            popcorn = popcorn | popcorns[i]
    if len(popcorn) == m:
        ans = min(ans, bit_count)
print(ans)
