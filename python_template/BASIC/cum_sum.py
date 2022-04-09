from typing import List


# 累積和
def cumsum(a: List[int]) -> List[int]:
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r


class OneDimSum:
    def __init__(self, a: List[int]) -> None:
        self.s = [0]
        for v in a:
            self.s.append(self.s[-1] + v)

    def solve(self, left: int, right: int) -> int:
        # 1-indexed
        return self.s[right] - self.s[left - 1]
