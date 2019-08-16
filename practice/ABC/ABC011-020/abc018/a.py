a = []
for i in range(1, 4):
    a.append([int(input()), i])
a.sort(reverse=True)

ans = [0] * 3
for i in range(3):
    ans[a[i][1]-1] = i+1
for i in range(3):
    print(ans[i])