# import pprint
h, w = map(int, input().split())
c = []
for _ in range(h):
    c.append(list(input()))
n = min(h, w)
# print(n)
# 斜めに走査して奇数回#が連続したらi // 2 + 1個目にフラグを建てる

flags = [[[0 for _ in range(n + 1)] for _ in range(w)] for _ in range(h)]

# 左上から右下

for k in range(-w, h):
    i = k
    j = 0
    count = 0
    while i < h and j < w:
        if i >= 0 and i < h and j >= 0 and j < w and c[i][j] == "#":
            count += 1
            if count > 2 and count % 2 == 1:
                length = count // 2
                flags[i - length][j - length][count] = 1
        else:
            count = 0
        i += 1
        j += 1
        # print(i, j)

ans = [0 for _ in range(n)]

for k in range(-w, h):
    j = w - 1
    i = k
    count = 0
    while i < h and j >= 0:
        if i >= 0 and i < h and j >= 0 and j < w and c[i][j] == "#":
            count += 1
            if count > 2 and count % 2 == 1:
                length = count // 2
                if flags[i - length][j + length][count] > 0:
                    ans[length - 1] += 1
        else:
            count = 0
        i += 1
        j -= 1
        # print(i, j)

# pprint.pprint(flags)
print(" ".join(map(str, ans)))