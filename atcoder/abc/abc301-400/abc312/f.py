import heapq
import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
INF = 10**20

n, m = map(int, input().split())
tx = []

can_without_opener = []
can_with_opener = []
openers = []
for _ in range(n):
    t, x = map(int, input().split())
    if t == 0:
        can_without_opener.append(x)
    elif t == 1:
        can_with_opener.append(x)
    else:
        openers.append(x)

can_without_opener.sort(reverse=True)  # 満足度が高いものから
can_with_opener.sort(reverse=True)  # 満足度が高いものから
openers.sort(reverse=True)  # 多く開けられるものから
can_with_opener = deque(can_with_opener)

# 缶抜きの数を累積和で管理する
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r


openers_cumsum = cumsum(openers)

sum_value = 0
choices = []
for i in range(min(m, len(can_without_opener))):
    x = can_without_opener[i]
    choices.append(x)
    sum_value += x
heapq.heapify(choices)

ans = sum_value
# ansの初期値は、缶抜きを使わない場合の満足度の合計
for i in range(1, min(m, len(openers) + 1)):
    # 缶抜きの選択数i個 (1からm - 1まで)
    # 残りの最適は簡単にもとまる
    stock = m - i
    can_open_count = openers[i - 1]
    # pushとpullの時に合計値を管理する
    # can_open_count缶を追加する
    for _ in range(can_open_count):
        if len(can_with_opener) > 0:
            x = can_with_opener.popleft()
            heapq.heappush(choices, x)
            sum_value += x
        else:
            break
    # 満足度が低い缶を取り出す
    while len(choices) > stock:
        x = heapq.heappop(choices)
        sum_value -= x
    ans = max(ans, sum_value)
print(ans)
