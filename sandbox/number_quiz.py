# 数字パズルゲームのプログラム
"""
問題文
数列Aの要素を全部使って数字Xを作ることができるかを判定してください。
ただし、数列Aの要素は一度だけ使うことができます。
作成することができる場合はYesとその例を、作成することができない場合はNoを出力してください。
制約
1 <= N <= 10**5
1 <= X <= 10**9
1 <= Ai <= 10**9
```input
N X
A1 A2 ... AN
```
N: number of numbers
X: answer of the quiz
A: list of numbers
"""

from typing import List

n, x = map(int, input().split())
a = list(map(int, input().split()))


def solve(a: List[int], x: int) -> str:
    """
    数列Aを入れた時に数字Xを作ることができるかを判定する
    # 括弧, 四則演算, (階乗), (累乗), (平方根), (対数), (三角関数), (絶対値), (最大値), (最小値)
    Args:
        a (List[int]): 数字列
        x (int): 答えとなる数字
    Returns:
        str: (Yes & answer) or No
    """
    pass
