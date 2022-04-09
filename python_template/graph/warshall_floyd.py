from typing import List


def warshall_floyd(n: int, d: List[List[int]]) -> List[List[int]]:
    # 空間計算量: O(n^2)
    # 時間計算量: O(n^3)
    # よって、n <= 10^2程度が限界
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
