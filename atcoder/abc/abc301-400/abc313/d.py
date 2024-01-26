from collections import defaultdict

n, k = map(int, input().split())
memo = defaultdict(lambda: -1)
each_group = defaultdict(lambda: -1)

# 隠された1/0からなる数列Aを特定するインタラクティブ問題
def answer(a):
    out = "! " + " ".join(list(map(str, a)))
    print(out)


def question(a):
    a_str = " ".join(sorted(list(map(str, a))))
    if memo[a_str] != -1:
        return memo[a_str]
    out = "? " + a_str
    print(out)
    res = int(input())
    memo[a_str] = res
    return res


# グループ分けを行なう
# 1をgroup1とする
groups = [[1], []]
each_group[1] = 0
x1 = question([i for i in range(1, k + 1)])
# 次で2〜K + K + iまで
# 手数ここまでで N - K + 1
base_a = [i for i in range(2, k + 1)]
for i in range(k + 1, n + 1):
    x_i = question(base_a + [i])
    if x_i == x1:
        groups[0].append(i)
        each_group[i] = 0
    else:
        groups[1].append(i)
        each_group[i] = 1

base_seq = [i for i in range(1, k + 2)]
for i in range(2, k + 1):
    a = []
    for x in base_seq:
        if x != i:
            a.append(x)
    xi = question(a)
    xj = question([j for j in range(1, k + 1)])
    if xi == xj:
        # iとjは同じ値
        groups[each_group[k + 1]].append(i)
        each_group[i] = each_group[k + 1]
    else:
        # iとjは異なる値
        groups[each_group[k + 1] ^ 1].append(i)
        each_group[i] = each_group[k + 1] ^ 1
# 全部でN回の質問
a0 = [0 for _ in range(n)]
a1 = [0 for _ in range(n)]

for i in range(1, n + 1):
    if each_group[i] == 0:
        a1[i - 1] = 1
    else:
        a0[i - 1] = 1

# どちらが正解か今までのmemoから判定する
count_a0 = 0
count_a1 = 0
for q in memo.keys():
    xq = memo[q]
    q_list = list(map(int, q.split()))
    sum_q0 = 0
    sum_q1 = 0
    for q_i in q_list:
        sum_q1 += a1[q_i - 1]
        sum_q0 += a0[q_i - 1]
    if sum_q1 % 2 == xq:
        count_a1 += 1
    if sum_q0 % 2 == xq:
        count_a0 += 1

if count_a0 == n:
    answer(a0)
else:
    answer(a1)
