n = int(input())
s = input()
t = input()

flag = True
for i in range(n):
    if s[i] == t[i]:
        continue
    if s[i] == "l" and t[i] == "1":
        continue
    if s[i] == "1" and t[i] == "l":
        continue
    if s[i] == "0" and t[i] == "o":
        continue
    if s[i] == "o" and t[i] == "0":
        continue
    flag = False
    break
print(["No", "Yes"][flag])
