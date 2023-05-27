n, h = map(int, input().split())
td = []
for _ in range(n):
    t, d = map(int, input().split())
    td.append([t, t * d])
td.sort()
td_list = [td[0]]
for t, d_sum in td[1:]:
    if d_sum > td[-1][1]:
        td_list.append([t, d_sum])
td_list.reverse()
# 2分探索する
# iターンまでの間に倒す方法があるか

def solve(turn):
    # 最初の方の最適はjターン目までに出せるダメージの最大
    current_turn = turn
    damage_sum = 0
    for i in range(len(td_list)):
        if td_list[i][0] > current_turn:
            continue
        damage_sum += td_list[i][1] * (current_turn - td_list[i][0] + 1)
        current_turn = td_list[i][0] - 1
        if damage_sum >= h:
            print("yes", turn, damage_sum)
            return True
    print("no", turn, damage_sum)
    return False

r = h # hターン掛ければ絶対倒せる
l = 0
m = (r + l) // 2
# めぐる式二分探索
while r - l > 1:
    print(l, m, r)
    m = (r + l) // 2
    if solve(m):
        r = m
    else:
        l = m
print(r)