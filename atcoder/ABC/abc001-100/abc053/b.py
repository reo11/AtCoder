s = str(input())
a = -1
z = 0

for i in range(len(s)):
    if a == -1 and s[i] == "A":
        a = i
    if s[i] == "Z":
        z = i
print(z - a + 1)
