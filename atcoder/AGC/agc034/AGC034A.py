n, a, b, c, d = map(int, input().split())
s = str(input())

flag = True
# B -> D
s_bd = s[b : d - 1]
for i in range(len(s_bd) - 1):
    if s_bd[i : i + 2] == "##":
        flag = False
        break
# A -> C
s_ac = s[a : c - 1]
if flag:
    for i in range(len(s_ac) - 1):
        if s_ac[i : i + 2] == "##":
            flag = False
            break

print(s_bd)
print(s_ac)

# Bのせいで通れ無い
has_ddd = False
if flag and len(s_bd) >= 2 and s_bd[-1] == "#":
    for i in range(len(s_bd) - 2):
        if s_bd[i : i + 3] == "...":
            has_ddd = True
    if not has_ddd:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
