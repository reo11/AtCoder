n = int(input())
kuku = []
s_ = 0
for i in range(1, 10):
    for j in range(1, 10):
        kuku.append(["{} x {}".format(i, j), i * j])
        s_ += i * j

m = s_ - n
ans = []
for name, v in kuku:
    if v == m:
        ans.append(name)
ans.sort()
print("\n".join(ans))
