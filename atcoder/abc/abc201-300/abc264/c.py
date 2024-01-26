import itertools

h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]

h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]


# 使用する行と列に1を立ててbit探索

for h_candidate in itertools.combinations(range(h1), h2):
    for w_candidate in itertools.combinations(range(w1), w2):
        flag = True
        for hi, hj in enumerate(h_candidate):
            for wi, wj in enumerate(w_candidate):
                if a[hj][wj] != b[hi][wi]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print("Yes")
            exit()
print("No")
