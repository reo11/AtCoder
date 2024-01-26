s = list(input())

# 26進数表記と捉える
# 逆順にして26**nにする

ans = 0
s.reverse()
for i in range(len(s)):
    ans += (ord(s[i]) - ord("A") + 1) * (26**i)
print(ans)
