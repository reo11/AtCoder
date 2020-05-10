s = input()
t = input()

f = True
for i in range(len(s)):
    if s[i] != t[i]:
        f = False
if len(s) + 1 != len(t):
    f = False
if f:
    print("Yes")
else:
    print("No")