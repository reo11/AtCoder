s = list(input())
ans = []
ex = set(["a", "i", "u", "e", "o"])

for si in s:
    if si in ex:
        continue
    ans.append(si)
print("".join(ans))
