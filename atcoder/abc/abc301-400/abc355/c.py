from collections import defaultdict
n, t = map(int, input().split())
a = list(map(int, input().split()))

# bingo
# 関係するところだけ更新する
# どれかが0になったら、その時点で終了

bingos = defaultdict(lambda: 0)

ans = -1

for i, ai in enumerate(a, 1):
    ai -= 1
    # 行番号 row_{i}
    # 列番号 col_{i}
    # 左上から右下への対角線番号 diag
    # 右上から左下への対角線番号 diag2

    row_i = ai // n
    col_i = ai % n

    bingos[f"row_{row_i}"] += 1
    bingos[f"col_{col_i}"] += 1

    if bingos[f"row_{row_i}"] == n or bingos[f"col_{col_i}"] == n:
        ans = i
        break

    if row_i == col_i:
        bingos["diag"] += 1
        if bingos["diag"] == n:
            ans = i
            break

    if row_i == n - col_i - 1:
        bingos["diag2"] += 1
        if bingos["diag2"] == n:
            ans = i
            break
print(ans)

