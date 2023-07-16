s = str(input())

count = 0
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        count += 1
print(count)
