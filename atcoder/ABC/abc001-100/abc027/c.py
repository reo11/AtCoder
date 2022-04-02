n = int(input())
d = 1
n_ = 1
while n_ <= n:
    n_ *= 2
    d += 1
else:
    d -= 1

if d % 2 == 0:
    t = [lambda x: 2 * x, lambda x: 2 * x + 1]
else:
    t = [lambda x: 2 * x + 1, lambda x: 2 * x]

n_ = 1
c = 0
while n_ <= n:
    n_ = t[c % 2](n_)
    c += 1

if c % 2:
    print("Aoki")
else:
    print("Takahashi")
