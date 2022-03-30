# Dubious Document 2
s_d = list(str(input()))
t = list(str(input()))

def check(s, t):
    flag = True
    for j in range(len(t)):
        if s[j] == t[j] or s[j] == "?":
            continue
        else:
            flag = False
    return flag

flag = False
for i in range(len(s_d) - len(t)+1):
    flag = check(s_d[len(s_d) - i - len(t):len(s_d) - i], t)
    if flag:
        for idx, j in enumerate(range(len(s_d) - i - len(t), len(s_d)-i)):
            s_d[j] = t[idx]
        break
for i in range(len(s_d)):
    if s_d[i] == "?":
        s_d[i] = "a"
if flag:
    print("".join(s_d))
else:
    print("UNRESTORABLE")

