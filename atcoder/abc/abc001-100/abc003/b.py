s = input()
t = input()

flag = True

atcoder = list(str("atcoder"))

for i in range(len(s)):
    if s[i] == t[i]:
        continue
    if s[i] == "@" and t[i] in atcoder:
        continue
    if t[i] == "@" and s[i] in atcoder:
        continue
    flag = False
    break
if flag:
    print("You can win")
else:
    print("You will lose")
