s = str(input())
sum_ = 0

for i in range(2 ** (len(s) - 1)):
    l = []
    for b in range(len(s)):
        bit = 2**b
        if i & bit > 0:
            l.append(b)
    if len(l) == 0:
        cal_l = [int(s)]
    else:
        pre = 0
        cal_l = []
        for index in l:
            cal_l.append(int(s[pre : index + 1]))
            pre = index + 1
        cal_l.append(int(s[pre:]))
    sum_ += sum(cal_l)
print(sum_)
