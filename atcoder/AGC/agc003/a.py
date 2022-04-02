from collections import defaultdict

s = input()
d = defaultdict(lambda: 0)
for c in s:
    d[c] += 1

if d["N"] > 0:
    if d["S"] == 0:
        print("No")
        exit()
if d["S"] > 0:
    if d["N"] == 0:
        print("No")
        exit()
if d["W"] > 0:
    if d["E"] == 0:
        print("No")
        exit()
if d["E"] > 0:
    if d["W"] == 0:
        print("No")
        exit()

print("Yes")
