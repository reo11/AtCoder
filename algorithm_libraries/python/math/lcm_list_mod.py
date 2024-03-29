# https://atcoder.jp/contests/abc152/tasks/abc152_e
from collections import defaultdict
from typing import Dict, List


class LCM_mod:
    """
    最小公倍数の計算を行う
    オーバーフローが発生しないように素因数分解し,
    因数の積を逐次余りに置き換えて最小公倍数を導出する.
    """

    def __init__(self, max_num: int, p: int = 10**9 + 7) -> None:
        self.max_num = max_num + 1
        self.p = p
        self.prime = [0 for _ in range(self.max_num)]
        self.max_map: Dict[int, int] = defaultdict(int)
        self.sieve()

    def rep_sqr(self, base: int, k: int) -> int:
        # 繰り返し二乗法
        ans = 1
        while k > 0:
            if k & 1:
                ans = ans * base % self.p
            base = base * base % self.p
            k >>= 1
        return ans

    def sieve(self) -> None:
        """
        エラトステネスの篩　O(n)
        nまでに含まれる素数を導出
        """
        self.prime[0], self.prime[1] = 1, 1
        for i in range(2, self.max_num):
            if self.prime[i] == 0:
                for j in range(i * 2, self.max_num, i):
                    if self.prime[j] == 0:
                        self.prime[j] = i
                self.prime[i] = i

    def lcm_list_mod(self, arr: List[int]) -> int:
        """
        listのそれぞれの要素について、素因数分解する
        それぞれの因数について最大であれば更新する
        """
        for i in range(len(arr)):
            num = arr[i]
            d: Dict[int, int] = defaultdict(int)

            while num > 1:
                fact = self.prime[num]
                d[fact] += 1
                num //= fact

            for i in d.keys():
                self.max_map[i] = max(self.max_map[i], d[i])

        ans = 1
        for i in self.max_map.keys():
            ans = (ans * self.rep_sqr(i, self.max_map[i])) % self.p
        return ans
