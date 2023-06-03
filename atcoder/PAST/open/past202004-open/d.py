s = input()

def aug(s):
    outs = []
    for i in range(2**len(s)):
        out = ['' for _ in range(len(s))]
        for j in range(len(s)):
            if i >> j & 1:
                out[j] = '.'
            else:
                out[j] = s[j]
        outs.append("".join(out))
    return outs
ans = []
for i in range(len(s)):
    for l in range(1, min(4, len(s)-i+1)):
        ans.extend(aug(s[i:i+l]))

print(len(set(ans)))