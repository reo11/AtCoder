import numpy as np
n = int(input())

s = []

for i in range(n):
    s.append(input())

for i in range(n):
    s_ = ""
    for j in range(n):
        s_ += s[n-j-1][i]
    print(s_)