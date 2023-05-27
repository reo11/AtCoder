n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
sum_a = sum(a)


def solve1(n, k, a):
    max_a = 10 ** 5
    dp = [[False] * (max_a) for _ in range(n + 1)]
    # dp[i][j] := i番目までの数を使ってjを作れるか
    dp[0][0] = True
    for i in range(n):
        for j in range(max_a):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + a[i] < max_a:
                    dp[i + 1][j + a[i]] = True

    ans = []
    for i in range(1, max_a):
        if not dp[n][i]:
            ans.append(i)
        if len(ans) == k:
            break
    current_ans_len = len(ans)
    if current_ans_len < k:
        for i in range(1, k - current_ans_len + 1):
            ans.append(sum(a) + i)
    return ans

def solve2(n, k, l):
    def make_combination(l):
        result = [0]
        for v in l:
            current_result_length = len(result)
            for j in range(current_result_length):
                result.append(v + result[j])
            result = list(set(result))
            result.sort()
        return result

    # 前後半で半分全列挙
    l_list = l[: len(l) // 2]
    r_list = l[len(l) // 2 :]
    all_l = sorted(make_combination(l_list))
    all_r = sorted(make_combination(r_list))

    r_diff = set()
    for i in range(1, len(all_r)):
        r_diff.add(all_r[i] - all_r[i - 1])

    inv_l = []
    max_l = min(max(r_diff), max(all_l) + k)
    set_l = set(all_l)
    for i in range(max_l + 1):
        if i not in set_l:
            inv_l.append(i)

    con_l = 0
    for i in range(1, len(all_l)):
        if all_l[i] - all_l[i - 1] == 1:
            con_l += 1
        else:
            break

    ans = []
    for i in range(1, len(all_r)):
        if all_r[i] - all_r[i - 1] <= con_l - 1:
            continue

        for j in inv_l:
            if all_r[i - 1] + j < all_r[i]:
                ans.append(all_r[i - 1] + j)
        if len(ans) >= k:
            break

    # 最大値より大きい
    # print(all_l)
    # print(all_r)
    # print(ans)
    currrent_ans_len = len(ans)
    if currrent_ans_len >= k:
        return ans[:k]
    for i in range(1, k - currrent_ans_len + 1):
        ans.append(all_l[-1] + all_r[-1] + i)
    return ans[:k]

def solve3(n, k, l):
    ans = []
    current_num = 1
    while len(ans) < k:
        # current_num以上で最小のXを探す
        ans.append()

ans = solve1(n, k, a)
# print(dp[-1][:20])
print(*ans, sep=" ")