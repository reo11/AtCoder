from typing import Iterator, List


def bit_full_search(max_bit: int) -> Iterator[List[int]]:
    for i in range(2 ** max_bit):
        bit_list = [0 for _ in range(max_bit)]
        for j in range(max_bit):
            if i & (2 ** j) > 0:
                bit_list[max_bit - j - 1] = 1
        yield bit_list


# bit全探索、カッコの条件で追加するか判定
def solve(bit_list: List[int]) -> str:
    ans = ""
    count = 0
    for v in bit_list:
        if v == 0:
            # (
            count += 1
            ans += "("
        else:
            # )
            count += -1
            ans += ")"
        if count < 0:
            return ""
    if count == 0:
        return ans
    else:
        return ""


n = int(input())
ans = []
for bit_list in bit_full_search(n):
    ans.append(solve(bit_list))
ans = list(filter(lambda x: x != "", ans))
ans = sorted(ans)
print("\n".join(ans))
