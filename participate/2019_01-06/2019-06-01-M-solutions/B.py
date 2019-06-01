s = str(input())

count = 0
for c in list(s):
    if c == "o":
        count += 1
if 15 - len(s) + count >= 8:
    print("YES")
else:
    print("NO")