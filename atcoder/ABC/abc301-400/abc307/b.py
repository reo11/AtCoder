n = int(input())
s = []
flag = False
for _ in range(n):
    s_i = list(input())
    s.append(s_i)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        s_concat = s[i] + s[j]
        r_s_con = reversed(s_concat)
        if "".join(s_concat) == "".join(r_s_con):
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")
