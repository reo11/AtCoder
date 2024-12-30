n = int(input())
sc = dict()
names = []
sum_c = 0
for _ in range(n):
    s, c = input().split()
    c = int(c)
    sum_c += c
    sc[s] = c
    names.append(s)
names.sort()

print(names[sum_c % n])
