x = int(input())
d = []
for i in range(-1000, 1000):
    d.append([i**5, i])

for j in range(len(d)):
    for i in range(len(d)):
        tmp = d[i][0] - d[j][0]
        if x == tmp:
            print(d[i][1], d[j][1])
            exit()
