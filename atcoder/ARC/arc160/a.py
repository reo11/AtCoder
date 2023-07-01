from pprint import pprint

n, k = map(int, input().split())
a = list(map(int, input().split()))


def solve1(a, k):
    # 全列挙
    # 愚直解
    b_list = []
    for l in range(n):
        for r in range(l, n):
            b = a
            b = b[:l] + b[l : r + 1][::-1] + b[r + 1 :]
            b_list.append(b)
    b_list.sort()
    pprint(b_list)
    return b_list[k - 1]


print(solve1(a, k))
