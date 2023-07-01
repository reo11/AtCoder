n = int(input())
s = input()

ans_list = []
for i in range(1, n):
    ans = 0
    count = 0
    for j in range(n - i):
        if s[j] == s[j + i]:
            count = 0
            break
        else:
            count += 1
        ans = max(ans, count)
    ans_list.append(ans)

print(*ans_list, sep="\n")
