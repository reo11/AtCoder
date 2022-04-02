n, a, b, c, d = map(int, input().split())
s = str(input())

flag = True

# c < dならbを先にゴールさせれば良い
s_bd = s[b : d - 1]
for i in range(len(s_bd) - 1):
    if s_bd[i : i + 2] == "##":
        flag = False
        break
s_ac = s[a : c - 1]
for i in range(len(s_ac) - 1):
    if s_ac[i : i + 2] == "##":
        flag = False
        break

if c > d:
    # ゴールの左が#
    if s[d - 2] == "#":
        s_bd = s[b - 2 : d]
        has_ddd = False
        for i in range(len(s_bd) - 2):
            if s_bd[i : i + 3] == "...":
                has_ddd = True
        if has_ddd == False:
            flag = False

if flag:
    print("Yes")
else:
    print("No")
