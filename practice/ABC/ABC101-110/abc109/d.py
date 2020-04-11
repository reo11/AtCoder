h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]

i = 0
j = 0
direction = 'r'
ans = []
route = []
is_selected = False
cnt = 0
while True:
    if cnt >= h * w:
        break
    next_i = i
    next_j = j
    if j == 0 and direction == 'l':
        next_i = i + 1
        direction = 'r'
    elif j == w-1 and direction == 'r':
        next_i = i + 1
        direction = 'l'
    else:
        if direction == 'r':
            next_j += 1
        else:
            next_j -= 1

    if a[i][j] % 2 == 1:
        if is_selected:
            ans.extend(route)
            route = []
            is_selected = False
        else:
            route.append([i+1, j+1, next_i+1, next_j+1])
            is_selected = True
    else:
        if is_selected:
            route.append([i+1, j+1, next_i+1, next_j+1])
    i = next_i
    j = next_j
    cnt += 1


print(len(ans))
for i in range(len(ans)):
    print(" ".join(list(map(str, ans[i]))))
