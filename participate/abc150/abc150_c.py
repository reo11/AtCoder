import itertools
n = int(input())
a_ = list(map(int, input().split()))
q_ = list(map(int, input().split()))
a = ""
q = ""
for i in range(n):
    a += str(a_[i])
    q += str(q_[i])

l = list(map(str, range(1, n+1)))
p = itertools.permutations(l, n)

d_ = []
for v in p:
    str_ = ""
    for c in v:
        str_ += str(c)
    d_.append(str_)
d_.sort()

dict_ = {}
for i, v in enumerate(d_):
    dict_[v] = i + 1

print(abs(dict_[a] - dict_[q]))