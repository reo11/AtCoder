from collections import defaultdict

MOD = 998244353
n = int(input())
s = input()


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if i == n:
            continue
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                if n // i == n:
                    continue
                divisors.append(n // i)
    return divisors


# 約数列挙
divs = make_divisors(n)
divs = sorted(divs)
# print(divs)

# 通りの数dp
# dp = [[0 for _ in range(len(divs))] for _ in range(n + 1)]
# # dp[i][j] = i文字目まで見たときに、約数divs[j]の周期を使用する場合の数
# for i in range(len(divs)):
#     dp[0][i] = 1

# for i in range(1, n + 1):
#     for j in range(len(divs)):
#         if s[i - 1] == "#":
#             # 高橋くんが出勤している場合どちらもよい
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = dp[i - 1][j] + dp[i - divs[j]][j]

counter = defaultdict(int)
shift_list = [[False for _ in range(div)] for div in divs]
for i in range(n):
    s_i = s[i]
    for j in range(len(divs)):
        div = divs[j]
        if s_i == ".":
            # 高橋くんが出勤していないなら必ず行く
            shift_list[j][i % div] = True

ans = 0
dived = defaultdict(lambda: [])
# それまでに出た約数の重複がない出現数をメモ化
for i in range(len(divs)):
    div = divs[i]
    ans_i = 1
    for is_shift in shift_list[i]:
        if not is_shift:
            ans_i *= 2
            ans_i %= MOD
    # 重複分削除
    for k, v in dived.items():
        if div % k == 0:
            ans_i -= v
            ans_i %= MOD
    dived[div] = ans_i
    ans += ans_i
    ans %= MOD
# print(dived)
print(ans)
