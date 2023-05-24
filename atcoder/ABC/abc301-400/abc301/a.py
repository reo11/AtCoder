n = int(input())
s = input()
ans = ""
count = [0, 0]
for i in range(n):
    if s[i] == "T":
        count[0] += 1
    else:
        count[1] += 1
    if count[0] > count[1]:
        ans = "T"
    elif count[1] > count[0]:
        ans = "A"
print(ans)