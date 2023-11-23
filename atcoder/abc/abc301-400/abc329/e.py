from collections import deque
n, m = map(int, input().split())
s = list(input())
t = input()

t_set = set([t])

for left_i in range(m):
    for right_i in range(m - left_i + 1):
        t_set.add("#" * left_i + t[left_i:left_i + right_i] + "#" * (m - left_i - right_i))
t_set.discard("#" * m)

def all_sharp(s):
    for i in range(len(s)):
        if s[i] != "#":
            return False
    return True

queue = deque()
for start_i in range(len(s) - len(t) + 1):
    if "".join(s[start_i:start_i + len(t)]) in t_set:
        queue.append((start_i))

while True:
    count = 0
    for start_i in range(len(s) - len(t) + 1):
        if "".join(s[start_i:start_i + len(t)]) in t_set:
            for j in range(start_i, start_i + len(t)):
                s[j] = "#"
            count += 1
    next_s = []
    streak = 0
    for si in s:
        if si == "#":
            streak += 1
            if streak < m:
                next_s.append(si)
        else:
            next_s.append(si)
            streak = 0

    if count == 0:
        break

if all_sharp(s):
    print("Yes")
else:
    print("No")