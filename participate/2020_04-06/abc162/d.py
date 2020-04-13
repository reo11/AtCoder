n = int(input())
s = input()

cnts = [0, 0, 0]
for i in range(n):
    if s[i] == 'R':
        cnts[0] += 1
    elif s[i] == 'G':
        cnts[1] += 1
    else:
        cnts[2] += 1

ans = cnts[0] * cnts[1] * cnts[2]

for i in range(n):
    for j in range(i+1, n):
        k = j + (j - i)
        if k >= n:
            continue
        if len(set([s[i], s[j], s[k]])) == 3:
            ans -= 1
print(ans)