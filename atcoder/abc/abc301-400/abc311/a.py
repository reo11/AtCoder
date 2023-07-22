n = int(input())
s = list(input())

counter = [0, 0, 0]

ans = 0
for i in range(len(s)):
    counter[ord(s[i]) - ord("A")] += 1
    if counter[0] > 0 and counter[1] > 0 and counter[2] > 0:
        ans = i + 1
        break
print(ans)
