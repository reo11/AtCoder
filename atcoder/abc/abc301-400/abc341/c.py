h, w, n = map(int, input().split())
t = list(input())

s = []
for i in range(h):
    s.append(list(input()))

# 全探索
count = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        pos = [i, j]
        flag = 1
        for ti in t:
            if s[pos[0]][pos[1]] == "#":
                flag = 0
                break
            if ti == "U":
                pos[0] -= 1
            elif ti == "D":
                pos[0] += 1
            elif ti == "L":
                pos[1] -= 1
            elif ti == "R":
                pos[1] += 1
            if s[pos[0]][pos[1]] == "#":
                flag = 0
                break
        count += flag
print(count)