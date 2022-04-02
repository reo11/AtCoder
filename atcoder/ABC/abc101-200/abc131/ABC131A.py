s = str(input())

flag = True
for i in range(3):
    if s[i] == s[i + 1]:
        flag = False

if flag:
    print("Good")
else:
    print("Bad")
