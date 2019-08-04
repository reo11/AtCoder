s = str(input())
n = len(s)
s_num = [1 for _ in range(n)]

# 右から
for i in range(n - 2):
    if s[i] == "R":
        if s[i+1] == "R":
            s_num[i+2] += s_num[i]
            s_num[i] = 0

# 左から
for i in range(n-2):
    i = n - i - 1
    if s[i] == "L":
        if s[i-1] == "L":
            s_num[i-2] += s_num[i]
            s_num[i] = 0
ans = list(map(str, s_num))
print(" ".join(ans))