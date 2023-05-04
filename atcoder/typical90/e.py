# import numpy as np
from collections import defaultdict

MOD = 10 ** 9 + 7

n, b, _k = map(int, input().split())
c = list(map(int, input().split()))

# 桁DP
# dp[上から何桁目][bで割った余り] = 通り数
# def solve1(n, b, c):
#     dp = [[0 for _ in range(b)] for _ in range(n + 1)]
#     # 無の状態は1パターンある（あまり0が無ければ遷移しないだけ）
#     # 上から見ていくので、前の桁数のあまりを10倍したあまりにすればいいだけ
#     # bは最大1000程度なので、上から1000桁くらいはこれで計算できる
#     # 実際は10^18桁あるので、ダブリングが必要
#     dp[0][0] = 1

#     for i in range(1, n + 1):
#         for c_k in c:
#             for j in range(b):
#                 next_mod = (j * 10 + c_k) % b
#                 dp[i][next_mod] += dp[i - 1][j]
#                 dp[i][next_mod] %= MOD
#     # print(dp)
#     return dp[n][0]

# def solve2(n, b, c):
#     # dpの遷移が行列累乗になるので、n桁目までをA^{2^m}の組み合わせで導出する

#     def dot(A, B):
#         # オーバーフローしないように自前実装（遅い）
#         n = len(A)
#         result = [[0 for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 for k in range(n):
#                     result[i][j] += (int(A[i][k]) % MOD) * (int(B[k][j]) % MOD)
#                     result[i][j] %= MOD
#         return np.array(result, dtype=np.uint64)

#     def multi_A(a, k):
#         # 正方行列か確認
#         assert len(a) == len(a[0])
#         size = len(a)
#         a = np.array(a, dtype=np.uint64)
#         # 行列Aのn乗を高速に求める
#         ans = np.identity(size, dtype=np.uint64)
#         while k > 0:
#             if k & 1:
#                 ans = dot(ans, a)
#             a = dot(a, a)
#             a = a % MOD
#             k >>= 1
#         return ans

#     a = np.zeros((b, b), dtype=np.uint64)
#     for i in range(b):
#         for c_k in c:
#             # i -> (i * 10 + c_k) % b に遷移する
#             # a[i][(i * 10 + c_k) % b] += 1
#             a[(i * 10 + c_k) % b][i] += 1

#     ma = multi_A(a, n)
#     # print(a)
#     # print(ma)
#     return int(ma[0][0]) % MOD


def solve3(n, b, c):
    # 10^mを前計算しておく
    ten_pow = [10 for _ in range(62)]
    for i in range(61):
        ten_pow[i + 1] = (ten_pow[i] * ten_pow[i]) % b

    dp = [[0 for _ in range(b)] for _ in range(62)]
    for c_k in c:
        dp[0][c_k % b] += 1
        dp[0][c_k % b] %= MOD

    for i in range(61):
        for j in range(b):
            for k in range(b):
                next_num = (j * ten_pow[i] + k) % b
                dp[i + 1][next_num] += dp[i][j] * dp[i][k]
                dp[i + 1][next_num] %= MOD

    # print(dp)
    ans = [0 for _ in range(b)]
    ans[0] = 1
    for i in range(61):
        if n >> i & 1:
            next_ans = [0 for _ in range(b)]
            for j in range(b):
                for k in range(b):
                    next_num = (j * ten_pow[i] + k) % b
                    next_ans[next_num] += ans[j] * dp[i][k]
                    next_ans[next_num] %= MOD
            ans = next_ans[:]
        # print(n, num, ans)
    # print(dp)
    return ans[0]


# print(solve1(n, b, c))
# print(solve2(n, b, c))
print(solve3(n, b, c))
