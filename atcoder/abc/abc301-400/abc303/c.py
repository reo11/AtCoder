n, m, hp, k = map(int, input().split())
s = list(input())
xy = set()
for _ in range(m):
    x, y = map(int, input().split())
    xy.add(f"{x}_{y}")

ans = True
current_pos = [0, 0]

for s_i in s:
    if hp <= 0:
        ans = False
        break
    if s_i == "R":
        current_pos[0] += 1
    elif s_i == "L":
        current_pos[0] -= 1
    elif s_i == "U":
        current_pos[1] += 1
    else:
        current_pos[1] -= 1
    hp -= 1
    # 移動した先に回復アイテムがある
    if f"{current_pos[0]}_{current_pos[1]}" in xy:
        if k > hp:
            hp = k
            xy.discard(f"{current_pos[0]}_{current_pos[1]}")

print(["No", "Yes"][ans])
