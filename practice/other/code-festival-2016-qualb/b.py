n, a, b = map(int, input().split())
s = input()

cnt_all = 0
cnt_for = 0
ans = []
for i in range(n):
    c = "No"
    if s[i] == "a" and cnt_all < a + b:
        cnt_all += 1
        c = "Yes"
    if s[i] == "b" and cnt_all < a + b and cnt_for+1 <= b:
        cnt_for += 1
        cnt_all += 1
        c = "Yes"
    ans.append(c)
print("\n".join(ans))