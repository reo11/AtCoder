from bisect import bisect_left, bisect_right
from collections import defaultdict, deque

n = int(input())
tx = []
posion_positions = defaultdict(lambda: deque())
ans = []
to_get = dict()
get_turns = set()
used_turns = set()
ans_k = 0
# 直近で手に入れた種類xのポーションを使用するのが保持すべき個数敵に最適
# なので拾う候補をキューに入れて、拾うべきポーションに印をつけていく
for turn in range(1, n + 1):
    t, x = map(int, input().split())
    tx.append((t, x))
    if t == 1:
        ans.append(0)
        posion_positions[x].append(turn)
    else:
        if len(posion_positions[x]) == 0:
            ans_k = -1
        else:
            get_turn = posion_positions[x].pop()
            get_turns.add(get_turn)
            used_turns.add(turn)

if ans_k == -1:
    print(-1)
    exit()
ans_k = 0
posion_in_hand = 0
get_idx = 0
for turn in range(1, n + 1):
    t, x = tx[turn - 1]
    if t == 1:
        if turn in get_turns:
            ans[get_idx] = 1
            posion_in_hand += 1
        get_idx += 1
    else:
        if turn in used_turns:
            posion_in_hand -= 1
    ans_k = max(ans_k, posion_in_hand)
print(ans_k)
print(*ans, sep=" ")
