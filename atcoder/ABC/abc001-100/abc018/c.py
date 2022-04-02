r, c, k = map(int, input().split())
s = []
for i in range(r):
    s.append(list(input()))

s_ = [[[0 for _ in range(2)] for _ in range(c)] for _ in range(r)]
for i in range(c):
    count = 0
    for j in range(r):
        if s[j][i] == "o":
            count += 1
        else:
            count = 0
        s_[j][i][0] = count
    count = 0
    for j in range(r)[::-1]:
        if s[j][i] == "o":
            count += 1
        else:
            count = 0
        s_[j][i][1] = count
ans = 0
for i in range(c):
    for j in range(r):
        flag = True
        for l in range(k):
            if i - l < 0 or i + l > c - 1:
                flag = False
                break
            if s_[j][i - l][0] < k - l or s_[j][i - l][1] < k - l:
                flag = False
                break
            if s_[j][i + l][0] < k - l or s_[j][i + l][1] < k - l:
                flag = False
                break
        if flag:
            ans += 1

print(ans)
