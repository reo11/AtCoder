from collections import Counter as C
r, c, k=map(int,input().split())
p = [0]*r
q = [0]*c
s = []
an = 0
for i in range(int(input())):
    a, b = map(int,input().split())
    p[a-1] += 1
    q[b-1] += 1
    s.append([a-1, b-1])
c = sorted(C(p).items(), key=lambda x: x[0])
d = C(q)
for i, j in c:
    if i > k:
        break
    else:
        an += d[k-i]*j
for i, j in s:
    if p[i] + q[j] == k:
        an -= 1
    elif p[i] + q[j] == k+1:
        an += 1
print(an)
