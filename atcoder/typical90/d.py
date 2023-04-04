import sys

input = sys.stdin.readline

h, w = map(int, input().split())

col_sum = [0 for _ in range(w)]
row_sum = [0 for _ in range(h)]
a = []
for i in range(h):
    a_w = list(map(int, input().split()))
    for j, v in enumerate(a_w):
        col_sum[j] += v
        row_sum[i] += v
    a.append(a_w)

ans_str = ""
ans = [["" for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = str(col_sum[j] + row_sum[i] - a[i][j])
    ans_str += " ".join(ans[i])
    if i < h - 1:
        ans_str += "\n"
print(ans_str)
