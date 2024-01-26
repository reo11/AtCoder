from collections import deque

n = int(input())
s = list(input())
a_list = []
b_list = []
INF = 10**10
for i in range(len(s)):
    s_i = s[i]
    if s_i == "A":
        a_list.append(i)
    else:
        b_list.append(i)
a_list = deque(a_list)
b_list = deque(b_list)

ans = []
mex_set = set()
mex_num = 0
for t in range(1, n + 1):
    # k回ターンtを行う
    # tが奇数の時Aliceが操作
    # tが偶数の時Bobが操作
    # AliceはsのBの最小値を選ぶのが最善
    # BobはsのAの最小値を選ぶのが最善
    # ターンtの最善は固定なので、順番に答えに入れていけば良い
    # mexの更新は全体でO(n)
    if t % 2 == 1:
        # Aliceのターン
        if len(b_list) > 0:
            min_value = b_list.popleft()
        else:
            min_value = INF
    else:
        # Bobのターン
        if len(a_list) > 0:
            min_value = a_list.popleft()
        else:
            min_value = INF
    mex_set.add(min_value)
    while mex_num in mex_set:
        mex_num += 1
    if s[mex_num] == "A":
        ans.append("Alice")
    else:
        ans.append("Bob")

print(*ans, sep="\n")
