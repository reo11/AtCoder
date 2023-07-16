s = str(input())
s2 = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
ans = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]

i = 0
off_set = 0
while True:
    if s2[off_set + i] == "B":
        off_set += 1
    if s == s2[off_set + i : off_set + i + 20]:
        print(ans[i])
        exit()
    else:
        i += 1
