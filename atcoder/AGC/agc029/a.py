s = input()
counter = {"W": 0, "B": 0}

ans = 0
for i in range(len(s)):
    if s[i] == "W":
        ans += counter["B"]
    counter[s[i]] += 1
print(ans)
