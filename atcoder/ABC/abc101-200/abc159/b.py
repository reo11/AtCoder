s = list(str(input()))
n = len(s)
ans = False
s1 = s
s2 = s[:(n-1)//2]
s3 = s[(n+3)//2-1:]
if s1 == s1[::-1] and s2 == s2[::-1] and s3 == s3[::-1]:
    ans = True
if ans:
    print("Yes")
else:
    print("No")