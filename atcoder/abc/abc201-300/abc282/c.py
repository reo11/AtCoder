n = int(input())
s = list(input())

flag = True
ans = []
for i in range(n):
    # ""で囲まれていない,を.にする
    if s[i] == "\"":
        flag = not flag

    if s[i] == "," and flag:
        ans.append(".")
    else:
        ans.append(s[i])
print("".join(ans))
