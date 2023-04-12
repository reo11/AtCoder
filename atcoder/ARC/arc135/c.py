n = int(input())
a = list(map(int, input().split()))

max_k = 30

# 全ビットの合計を計算しておく
bit_sum = [0 for _ in range(max_k)]
for a_i in a:
    for bit_i in range(max_k):
        # bit_i桁目のbitチェック
        bit_sum[bit_i] += (a_i >> bit_i) & 1

ans = 0
for x in [0] + a:
    ans_i = 0
    for bit_i in range(max_k):
        if (x >> bit_i) & 1:
            # xのbit_i桁目にbitが立っていた場合
            ans_i += (2 ** bit_i) * (n - bit_sum[bit_i])
        else:
            ans_i += (2 ** bit_i) * bit_sum[bit_i]
    ans = max(ans, ans_i)
print(ans)