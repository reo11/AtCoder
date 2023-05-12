t = int(input())
c = "codeforces"
t_ans = []
for _ in range(t):
    ans = 0
    s = input()
    for i in range(10):
        if c[i] != s[i]:
            ans += 1
    t_ans.append(ans)
print(*t_ans, sep="\n")