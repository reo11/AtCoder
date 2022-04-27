from collections import defaultdict
s = input()

large_chars = [chr(ord("A") + i) for i in range(26)]

def solve(text):
    d = defaultdict(lambda: 0)
    cnt = {
        "large": 0,
        "small": 0,
    }
    for c in list(text):
        d[c] += 1
        if d[c] > 1:
            return False
        if c in large_chars:
            cnt["large"] += 1
        else:
            cnt["small"] += 1
    if cnt["large"] > 0 and cnt["small"] > 0:
        return True
    else:
        return False

if solve(s):
    print("Yes")
else:
    print("No")
