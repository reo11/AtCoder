n, a, b = map(int, input().split())
s = list(input())
ss = s + s


def change_cost(s, b):
    # sを回文にするのにかかるコスト
    cost = 0
    for i in range(len(s) // 2):
        if s[i] == s[n - 1 - i]:
            continue
        else:
            cost += b
    return cost


ans = float("inf")
for start_i in range(n):
    ans = min(ans, change_cost(ss[start_i : start_i + n], b) + start_i * a)
print(ans)
