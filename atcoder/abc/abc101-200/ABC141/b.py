s = list(str(input()))
l1 = ["R", "U", "D"]
l2 = ["L", "U", "D"]

ans = "Yes"
for i, c in enumerate(s):
    if i % 2 == 0 and c not in l1:
        ans = "No"
    elif i % 2 == 1 and c not in l2:
        ans = "No"
print(ans)
