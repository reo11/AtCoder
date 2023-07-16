from collections import defaultdict

n = int(input())
s = input()
visited = defaultdict(lambda: defaultdict(lambda: False))
visited[0][0] = True

x = False
current_pos = [0, 0]
for i in range(n):
    c = s[i]
    if c == "R":
        current_pos[0] += 1
    elif c == "L":
        current_pos[0] -= 1
    elif c == "U":
        current_pos[1] += 1
    else:
        current_pos[1] -= 1
    if visited[current_pos[0]][current_pos[1]]:
        x = True
    visited[current_pos[0]][current_pos[1]] = True
print(["No", "Yes"][x])
