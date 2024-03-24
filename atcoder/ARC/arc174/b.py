import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

def is_avg_under_three(x_sum, x_count, buy_five, buy_four):
    score = (x_sum + 5 * buy_five + 4 * buy_four) // (x_count + buy_five + buy_four)
    return score < 3

def solve():
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    # 考察
    # 1, 2, 3を買うことは考える必要がない
    # 4と5の評価をどの程度買うか
    # 5が4より安い場合は4を買う必要がない

    x_sum = 0
    x_count = 0
    for i in range(5):
        x_count += a[i]
        x_sum += (i + 1) * a[i]
    ans = 0

    if x_sum // x_count >= 3:
        return 0

    if p[3] * 2 >= p[4]:
        # 購入数2分探索する
        l = 0
        r = 10 ** 18
        while r - l > 1:
            m = (l + r) // 2
            if is_avg_under_three(x_sum, x_count, m, 0):
                l = m
            else:
                r = m
        # print("a", x_sum, x_count, l, r, m)
        # 全部5だと多すぎる可能性があるので、5を一つ減らして、4を一つ買うケースを考える
        if r > 0 and not is_avg_under_three(x_sum, x_count, r - 1, 1):
            ans += min((r - 1) * p[4] + p[3], r * p[4])
        else:
            ans += r * p[4]
    else:
        # 購入数2分探索する
        l = 0
        r = 10 ** 18
        while r - l > 1:
            m = (l + r) // 2
            if is_avg_under_three(x_sum, x_count, 0, m):
                l = m
            else:
                r = m
        # print("b", x_sum, x_count, l, r, m)
        ans += r * p[3]
    # print(delta)
    return ans

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')