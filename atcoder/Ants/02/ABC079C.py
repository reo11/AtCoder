s = str(input())
a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])
ans = ""

for op1 in ["+", "-"]:
    for op2 in ["+", "-"]:
        for op3 in ["+", "-"]:
            sum_ = a
            if op1 == "+":
                sum_ += b
            else:
                sum_ -= b
            if op2 == "+":
                sum_ += c
            else:
                sum_ -= c
            if op3 == "+":
                sum_ += d
            else:
                sum_ -= d
            if sum_ == 7:
                ans = "{}{}{}{}{}{}{}=7".format(a, op1, b, op2, c, op3, d)
        if sum_ == 7:
            break
    if sum_ == 7:
        break
print(ans)
