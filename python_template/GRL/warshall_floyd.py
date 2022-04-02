def warshall_floyd(n, d):
    # 空間計算量: O(n^2)
    # 時間計算量: O(n^3)
    # よって、n <= 10^2程度が限界
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
