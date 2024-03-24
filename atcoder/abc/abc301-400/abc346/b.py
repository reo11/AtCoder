w, b = map(int, input().split())

s = "wbwbwwbwbwbw"
ss = ""
for i in range(100):
    ss += s

for i in range(len(ss) - w - b):
    count_w = 0
    count_b = 0
    for j in range(i, i + w + b):
        if ss[j] == "w":
            count_w += 1
        else:
            count_b += 1
    if count_w == w and count_b == b:
        print("Yes")
        exit()
print("No")