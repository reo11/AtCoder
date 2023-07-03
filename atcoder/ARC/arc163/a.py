
def solve():
    n = int(input())
    s = list(input())
    flag = False
    for i in range(1, n):
        s1 = "".join(s[:i])
        s2 = "".join(s[i:])
        if s1 < s2:
            flag = True
    return "Yes" if flag else "No"

t = int(input())
ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')