from collections import defaultdict, deque

n = int(input())
a = list(map(int, input().split()))

# 生成可能な部分列の数を数える
# 等差数列はまとめることができ、kで終わる数列をlv[k]で管理するとk+1出現時にどの数列に追加するかで分岐が発生する
# また、注意しないといけないのは、途中で成立しなくなるパターン
# そのindexを挟んだ部分列は成立しないので、数え上げを一度リセットする必要がある
# ps, やっぱりqueueで管理すると良さそう
ans = 0
queue = deque()
for i in range(n):
    a_i = a[i]
    if a_i > 1:
        # 直近のa_i - 1を使うのが最善のはず
        while len(queue) > 0 and queue[-1] != a_i - 1:
            queue.pop()
        if len(queue) > 0:
            queue.pop()  # a_i - 1を消す
            queue.append(a_i)
    else:
        queue.append(1)
    # a_i = Rとするパターン数をansに加算する
    ans += len(queue)  # 嘘っぽい
    # print(ans, queue)
# print(counter)
print(ans)
