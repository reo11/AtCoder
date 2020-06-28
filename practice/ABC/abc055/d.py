n = int(input())
s = list(map(lambda x: 0 if x == 'o' else 1, list(input())))
# o: 0, x: 1

def decode_animals(l):
    return "".join(list(map(lambda x: 'S' if x == 0 else 'W', animals)))

def check(first, second, pre_last, last, first_coment, last_coment):
    # 最初と最後の帳尻合わせ
    f1 = False
    if first == 0:
        if first_coment == 0:
            f1 = second == last
        else:
            f1 = second != last
    else:
        if first_coment == 0:
            f1 = second != last
        else:
            f1 = second == last
    f2 = False
    if last == 0:
        if last_coment == 0:
            f2 = first == pre_last
        else:
            f2 = first != pre_last
    else:
        if last_coment == 0:
            f2 = first != pre_last
        else:
            f2 = first == pre_last
    return f1 and f2

for i in range(4):
    animals = []
    for j in range(2):
        # S: 0, W: 1
        if i >> j & 1:
            animals.append(1)
        else:
            animals.append(0)
    for i in range(2, n):
        next_animal = 0
        if animals[i-1] == 0 and s[i-1] == 0 or animals[i-1] == 1 and s[i-1] == 1:
            next_animal = animals[i-2]
        elif animals[i-1] == 0 and s[i-1] == 1 or animals[i-1] == 1 and s[i-1] == 0:
            next_animal = [1, 0][animals[i-2]]
        animals.append(next_animal)
    if check(animals[0], animals[1], animals[-2], animals[-1], s[0], s[-1]):
        ans = decode_animals(animals)
        print(ans)
        exit()
print(-1)