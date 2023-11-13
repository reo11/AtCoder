s = []
for _ in range(9):
    si = list(input())
    s.append(si)
ans = 0
for window_size in range(1, 8):
    for i in range(9 - window_size + 1):
        for j in range(9 - window_size + 1):
            count = 0
            if i + window_size >= 9 or j + window_size >= 9:
                continue
            if s[i][j] == "#":
                count += 1
            if s[i][j + window_size] == "#":
                count += 1
            if s[i + window_size][j] == "#":
                count += 1
            if s[i + window_size][j + window_size] == "#":
                count += 1
            if count == 4:
                ans += 1
print(ans)