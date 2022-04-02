s = input()
n = len(s)

f = 0
for i in range(n):
    if s[i] == "C" and f == 0:
        f += 1
    if s[i] == "F" and f == 1:
        print("Yes")
        exit()
print("No")
