import math
from fractions import Fraction

N = int(input())

ta = [0] * N
ao = [0] * N

for i in range(N):
    t, a = map(int, input().split())
    if i == 0:
        ta[i] = t
        ao[i] = a
    else:
        tmp = max(math.ceil(Fraction(ta[i - 1], t)), math.ceil(Fraction(ao[i - 1], a)))
        ta[i] = t * tmp
        ao[i] = a * tmp

print(ta[-1] + ao[-1])
