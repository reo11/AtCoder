from collections import defaultdict

MOD = 998244353

n, k = map(int, input().split())
s = list(input())
memo = [[[0 for _ in range(k + 1)] for _ in range(k + 1)] for _ in range(k + 1)]
# ABCのみ
# 同じアルファベットを選んでも変化しないので相異なるアルファベットを選ぶ
# A-B, B-C, C-Aの3つの入れ替え方を考える
# また、手順kにおいてそれまでに実施した各入れ替えの回数から、1組が除外される
# 二項係数？

memo[0][0][0] = 1
ans = 1
counter = defaultdict(int)
for si in s:
    counter[si] += 1
for ki in range(1, k + 1):
    # ki: k回の入れ替えを行なう
    ansi = 0
    for abi in range(ki):
        for bci in range(ki - abi):
            for cai in range(ki - abi - bci):
                if abi + bci + cai != ki - 1:
                    continue
                ansi = 0
                # AB
                if counter["A"] - abi > 0 and counter["B"] - abi > 0:
                    v = (
                        memo[abi][bci][cai]
                        * (counter["A"] - abi)
                        * (counter["B"] - abi)
                    )
                    memo[abi + 1][bci][cai] += v
                    memo[abi + 1][bci][cai] %= MOD
                    ansi += v
                    ansi %= MOD
                # BC
                if counter["B"] - bci > 0 and counter["C"] - bci > 0:
                    v = (
                        memo[abi][bci][cai]
                        * (counter["B"] - bci)
                        * (counter["C"] - bci)
                    )
                    memo[abi][bci + 1][cai] += v
                    memo[abi][bci + 1][cai] %= MOD
                    ansi += v
                    ansi %= MOD
                # CA
                if counter["C"] - cai > 0 and counter["A"] - cai > 0:
                    v = (
                        memo[abi][bci][cai]
                        * (counter["C"] - cai)
                        * (counter["A"] - cai)
                    )
                    memo[abi][bci][cai + 1] += v
                    memo[abi][bci][cai + 1] %= MOD
                    ansi += v
                    ansi %= MOD
                ans += ansi
                ans %= MOD
ans = 0
for i in range(k + 1):
    for j in range(k + 1):
        for l in range(k + 1):
            ans += memo[i][j][l]
            ans %= MOD
print(ans)
sum_memo = defaultdict(lambda: False)
for i in range(ki):
    for j in range(ki - i):
        for l in range(ki - i - j):
            if i + j + l != ki - 1:
                continue
            if sum_memo[i + j + l]:
                continue
            sum_memo[i + j + l] = True
            if i + j + l == 0:
                continue
            print(i, j, l, memo[i][j][l])
            ans -= memo[i][j][l] * (i + j + l - 1)
            ans %= MOD
print(memo)
print(ans)
