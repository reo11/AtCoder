from collections import defaultdict, deque

t = int(input())


def solve(n, x, y):
    # x, y はABCからなる文字列
    # A...B...の順に変形する
    # y_tmpと同じになるように後ろから決めていく
    x = list(x)
    y = list(y)

    # Cのロックと置き換えを最初に行う
    # Cは境界になる
    counter_x = defaultdict(lambda: 0)
    counter_y = defaultdict(lambda: 0)
    xc_queue = deque()
    for i, (xi, yi) in enumerate(zip(x, y)):
        if yi == "C" and xi == "C":
            # Bの不足分を後ろから埋めていく
            # そのほかのCは全てAに置き換える
            while xc_queue:
                idx = xc_queue.pop()
                if counter_y["B"] > counter_x["B"]:
                    x[idx] = "B"
                    counter_x["B"] += 1
                    counter_x["C"] -= 1
                else:
                    x[idx] = "A"
                    counter_x["A"] += 1
                    counter_x["C"] -= 1
            if counter_x["A"] != counter_y["A"] or counter_x["B"] != counter_y["B"]:
                return "No"
            counter_x = defaultdict(lambda: 0)
            counter_y = defaultdict(lambda: 0)
        elif yi == "C" and xi != "C":
            return "No"
        else:
            counter_x[xi] += 1
            counter_y[yi] += 1
            if xi == "C":
                xc_queue.append(i)
    while xc_queue:
        idx = xc_queue.pop()
        if counter_y["B"] > counter_x["B"]:
            x[idx] = "B"
            counter_x["B"] += 1
            counter_x["C"] -= 1
        else:
            x[idx] = "A"
            counter_x["A"] += 1
            counter_x["C"] -= 1
    if counter_x["A"] != counter_y["A"] or counter_x["B"] != counter_y["B"]:
        return "No"

    # Bの数を数えて超えなければok
    counter = [0, 0]
    for xi, yi in zip(x, y):
        if xi == "C" or yi == "C":
            counter = [0, 0]
            continue
        if yi == "B":
            counter[1] += 1
        if xi == "B":
            counter[0] += 1
        if counter[0] > counter[1]:
            return "No"

    return "Yes"


ans = []
for _ in range(t):
    n, x, y = input().split()
    ans.append(solve(n, x, y))
print(*ans, sep="\n")
