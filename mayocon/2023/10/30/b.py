s = list(input())

flag = True

if s[0] != "A":
    flag = False

count_C = 0
for i in range(2, len(s) - 1):
    if s[i] == "C":
        count_C += 1
if count_C != 1:
    flag = False

count_small = 0
for si in s:
    if si.islower():
        count_small += 1

if count_small != len(s) - 2:
    flag = False

if flag:
    print("AC")
else:
    print("WA")
