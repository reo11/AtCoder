s = input()
k = int(input())

count = 0
num = -1
for i in range(len(s)):
    if s[i] == "1":
        count += 1
    else:
        num = int(s[i])
        break
if k > count:
    print(num)
else:
    print(1)