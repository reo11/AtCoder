from collections import defaultdict

s = list(input())
s = list(map(int, s))

counter = defaultdict(int)
for num in s:
    counter[num] += 1

cand = []
n = 8
while n <= 1000:
    if n < 1000:
        n_tmp = list(map(int, list(str(n).zfill(3))))
    else:
        n_tmp = list(map(int, list(str(n))))
    c = defaultdict(int)
    for i in n_tmp:
        c[i] += 1
    cand.append(c)
    n += 8

flag = False
if len(s) == 1:
    if s[0] % 8 == 0:
        flag = True
elif len(s) == 2:
    if (s[0] * 10 + s[1]) % 8 == 0 or (s[1] * 10 + s[0]) % 8 == 0:
        flag = True
else:
    for d in cand:
        flag_i = True
        for num, count in d.items():
            if counter[num] < count:
                flag_i = False
        if flag_i == True:
            flag = True

if flag:
    print("Yes")
else:
    print("No")
