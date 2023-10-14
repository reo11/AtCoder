from collections import defaultdict
n = int(input())
s = int(input())

def norm_for_s(s):
    zeropad_si = str(s).zfill(n)
    ll = list(zeropad_si)
    counter = [0 for _ in range(10)]
    for l in ll:
        counter[int(l)] += 1
    return counter

normed_s = norm_for_s(s)

ans = 0
for i in range(10 ** 7 + 1):
    if i * i > 10 ** (n + 1):
        break
    si = str(i * i).zfill(n)
    count = [0 for _ in range(10)]
    flag = True
    for j in range(len(si)):
        numi = int(si[j])
        count[numi] += 1
        if count[numi] > normed_s[numi]:
            flag = False
            break

    for j in range(10):
        if not flag or count[j] != normed_s[j]:
            flag = False
            break

    if flag:
        ans += 1
        # print(i, ans, i ** 2, count, normed_s)

print(ans)
