# 賢く全探索

v1, v2, v3 = map(int, input().split())

# 1は固定
a1 = 0
b1 = 0
c1 = 0

def calc(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # 3つの箱を置いた時のv1, v2, v3
    # v1はかぶってない体積
    # v2は2つの箱が被っている体積
    # v3は3つの箱が被っている体積


# 対称性を考慮して全探索
for a2 in range(21):
    for b2 in range(21):
        for c2 in range(21):
            for a3 in range(21):
                for b3 in range(21):
                    for c3 in range(21):
                        if a2 + b3 == v1 and a3 + b2 == v2 and b2 + c3 == v3:
                            print("Yes")
                            exit()