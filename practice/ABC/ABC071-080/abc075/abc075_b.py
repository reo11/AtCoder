h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(str(input())))

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            count = 0
            for i_ in range(-1, 2):
                if i + i_ < 0 or i + i_ >= h:
                    continue
                for j_ in range(-1, 2):
                    if j + j_ < 0 or j + j_ >= w:
                        continue
                    if i_ == 0 and j_ == 0:
                        continue
                    if s[i+i_][j+j_] == "#":
                        count += 1
            s[i][j] = str(count)
for i in range(h):
    print("".join(s[i]))
