from collections import deque
import math
n, l, r = map(int, input().split())

# (2**i)*j <= 2**i*(j+1) - 1の範囲の質問ができる
# [l, r]を上記の形式に分解する

# lとrを(2**i)*j ~ (2**i)*(j+1) - 1の形に分解して、そのリストを返す
def parse(l, r):
    res = deque()
    q = [[l, r]]

    while q:
        li, ri = q.pop()
        diff = ri - li
        if diff == 1:
            i = 0
            j = li
            res.append([i, j, li, ri])
            continue
        elif diff == 0:
            continue

        for x in range(math.ceil(math.log2(diff)) + 1, -1, -1):
            if 2 ** x > diff:
                continue

            # l以上でxの倍数である最小値を求める
            if li % (2 ** x) == 0:
                new_l = li
            else:
                new_l = li + (2 ** x - (li % (2 ** x)))
            new_r = new_l + 2 ** x
            if new_r > ri:
                continue
            else:
                i = x
                j = new_l // (2 ** i)
                res.append([i, j, new_l, new_r])
                q.append([li, new_l])
                q.append([new_r, ri])
                break
    res = sorted(list(res))
    return res

questions = parse(l, r + 1)
ans = 0

for i, j, li, ri in questions:
    # print(li, ri)
    print("?", i, j, flush=True)
    ret = int(input())
    if ret == -1:
        print("!", -1, flush=True) # エラー
    ans += ret
    ans %= 100

print("!", ans, flush=True)
