from collections import defaultdict
n, k = map(int, input().split())
s = list(input())
MOD = 998244353

# sはA, B, ?のいずれか
# k <= 10
# sの連続するk文字が回文でないものの数

# i文字目を決める時直近登場したk - 1文字までの組み合わせ数を記録しておいてDPする
kaibun = set()

for i in range(2**k):
    str_bin = str(bin(i))[2:].zfill(k)
    if str_bin == str_bin[::-1]:
        kaibun.add(int(str_bin, 2))
# print(kaibun)

# A=0, B=1として数字で管理
# 回文を含まない文字列の数で、末尾がjであるものを更新していく
counts = [0] * (n + 1) # k文字の文字列で回文を含まないものの数
counts[0] = 1
dp = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
for i, si in enumerate(s):
    add_count = 0
    if si == "A" or si == "?":
        dp[i][0][1] = counts[i]
        counts[i + 1] += counts[i]
    if si == "B" or si == "?":
        dp[i][1][1] = counts[i]
        counts[i + 1] += counts[i]
    counts[i + 1] %= MOD

    # 1ステップ前のdpで更新
    for num, step_counts in dp[i - 1].items():
        for step_count, count in step_counts.items():
            # 末尾にA, Bを足して更新
            if step_count < k - 1:
                if si == "A":
                    dp[i][num << 1][step_count + 1] += count
                    dp[i][num << 1][step_count + 1] %= MOD
                    counts[i + 1] += count
                elif si == "B":
                    dp[i][num << 1 + 1][step_count + 1] += count
                    dp[i][num << 1 + 1][step_count + 1] %= MOD
                    counts[i + 1] += count
                else:
                    dp[i][num << 1][step_count + 1] += count
                    dp[i][num << 1][step_count + 1] %= MOD
                    dp[i][num << 1 + 1][step_count + 1] += count
                    dp[i][num << 1 + 1][step_count + 1] %= MOD
                    counts[i + 1] += 2 * count
                counts[i + 1] %= MOD
            else:
                next_nums = []
                if si == "A":
                    next_nums.append(num << 1)
                elif si == "B":
                    next_nums.append(num << 1 + 1)
                else:
                    next_nums.append(num << 1)
                    next_nums.append(num << 1 + 1)
                for next_num in next_nums:
                    if next_num not in kaibun:
                        # 長さiの文字列で回文を含まないことが確定している数
                        counts[i + 1] += count
                        counts[i + 1] %= MOD
print(counts)