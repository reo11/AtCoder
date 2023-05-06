from collections import defaultdict
from typing import Dict


def cnt_multiple(s: str, p: int) -> int:
    # ABC158E, ABC164D
    n = len(s)
    if p != 2 and p != 5:
        a = []
        t = 1
        for i in range(n - 1, -1, -1):
            a.append((ord(s[i]) - ord("0")) * t % p)
            t = t * 10 % p
        cum = [0]
        for v in a:
            cum.append((cum[-1] + v) % p)

        dic: Dict[int, int] = defaultdict(int)
        ans = 0
        for v in cum:
            ans += dic[v]
            dic[v] += 1
        return ans
    elif p == 2:
        ans = 0
        for i in range(n):
            if (ord(s[i]) - ord("0")) % 2 == 0:
                ans += i + 1
        return ans
    else:
        ans = 0
        for i in range(n):
            if (ord(s[i]) - ord("0")) % 5 == 0:
                ans += i + 1
        return ans
