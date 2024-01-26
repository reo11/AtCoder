n = int(input())

flag = True
s = [input() for _ in range(n)]

s_set = set()
for i in range(n):
    si = s[i]
    # 3つめの条件
    if si in s_set:
        flag = False
        break
    s_set.add(si)

    if not si[0] in ["H", "D", "C", "S"]:
        flag = False
        break
    if not si[1] in ["A"] + list(map(str, range(2, 10))) + ["T", "J", "Q", "K"]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
