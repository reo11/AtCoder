n, m = map(int, input().split())
l_list = list(map(int, input().split()))

# 二分探索
left = max(l_list) - 1
right = sum(l_list) + len(l_list) - 1
# leftを成立しない最大、rightを成立する最小とする
while right - left > 1:
    window_size = (left + right) // 2
    # 最初は1行, 文字数は0
    row_count = 1
    current_size = 0
    for li in l_list:
        if li > window_size:
            break
        if current_size + li > window_size:
            row_count += 1
            current_size = li + 1
        else:
            current_size += li + 1
        # print(m, row_count, li, current_size)
    if row_count <= m:
        # m行以下で表示できる場合、window_sizeが大きすぎるのでwindow_sizeを小さくしていく
        right = window_size
    else:
        # m行以下で表示できない場合、window_sizeが小さすぎるのでwindow_sizeを大きくしていく
        left = window_size
print(right)
