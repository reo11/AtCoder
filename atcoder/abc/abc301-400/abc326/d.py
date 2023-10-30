import itertools
from collections import defaultdict, deque

n = int(input())
R = list(input())
C = list(input())

def first(a, b, c):
    min_value = min(a, b, c)
    if min_value == a:
        return "A"
    elif min_value == b:
        return "B"
    else:
        return "C"

def check_abc(a, b, c):
    # 衝突してないか
    for i in range(n):
        if a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
            return False
    # 条件1: 各行と列にA, B, Cが1つずつは候補生成でクリア
    # 条件2: Rのi文字目がi行目の最初の文字と一致
    for i in range(n):
        if R[i] != first(a[i], b[i], c[i]):
            return False

    # 条件3: Cのi文字目がi列目の最初の文字と一致
    l = [[] for _ in range(n)]
    for i in range(n):
        aj = a[i]
        bj = b[i]
        cj = c[i]
        l[aj].append([i, "A"])
        l[bj].append([i, "B"])
        l[cj].append([i, "C"])
    for i in range(n):
        l[i].sort()
        if C[i] != l[i][0][1]:
            return False
    return True

def show_abc(a, b, c):
    out = [["." for _ in range(n)] for _ in range(n)]
    for i in range(n):
        out[i][a[i]] = "A"
        out[i][b[i]] = "B"
        out[i][c[i]] = "C"
    return "Yes\n" + "\n".join(["".join(row) for row in out])

# 賢く全探索
abc_list = list(range(n))
for a, b, c in itertools.product(itertools.permutations(abc_list), repeat=3):
    if check_abc(a, b, c):
        print(show_abc(a, b, c))
        exit()
print("No")