n = int(input())

ans_set = set(list(range(1, (2 * n) + 2)))

while True:
    if len(ans_set) != 0:
        ansi = list(ans_set)[0]
        print(ansi, flush=True)
        ans_set.discard(ansi)
    x = int(input())
    if x == 0:
        exit()
    ans_set.discard(x)
