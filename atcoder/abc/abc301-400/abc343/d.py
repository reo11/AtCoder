from collections import defaultdict

n, t = map(int, input().split())
counter = defaultdict(lambda: 0)
numbers = defaultdict(lambda: 0)
ansi = set([0])
counter[0] = n

ans = []
for _ in range(t):
    a, b = map(int, input().split())
    player_num = numbers[a]
    counter[player_num] -= 1
    if counter[player_num] == 0:
        ansi.discard(player_num)
    numbers[a] = player_num + b
    counter[player_num + b] += 1
    if counter[player_num + b] == 1:
        ansi.add(player_num + b)
    ans.append(len(ansi))
    # print(counter, numbers, ansi, ans)
print(*ans, sep="\n")
