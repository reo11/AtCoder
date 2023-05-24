n, m, k = map(int, input().split())
s = list(input())
count_x = [0]
for i in range(n):
    if s[i] == "x":
        count_x.append(count_x[-1] + 1)
    else:
        count_x.append(count_x[-1])


def count_holiday(start_idx, holiday_count, yukyu):
    # start_idx: 1-indexed
    # holiday_count連休をstart_idxから作成可能か判定
    t_count = 1
    yukyu_needed = 0
    yukyu_needed += (
        count_x[min(n, start_idx + holiday_count - 1)] - count_x[start_idx - 1]
    )
    first_len = min(n - start_idx + 1, holiday_count)
    if n - start_idx + 1 < holiday_count:
        if holiday_count - first_len >= n:
            yukyu_needed += ((holiday_count - first_len) // n) * count_x[-1]
            t_count += (holiday_count - first_len) // n
        if (holiday_count - first_len) % n > 0:
            yukyu_needed += count_x[(holiday_count - first_len) % n]
            t_count += 1
    if yukyu_needed <= yukyu and t_count <= m:
        return True
    else:
        return False


def can(holiday_count, yukyu):
    flag = False
    for i in range(1, n + 1):
        flag = count_holiday(i, holiday_count, yukyu)
        if flag:
            break
    return flag


l = 0
r = n * m + 1
while r - l > 1:
    # print(l, r)
    mid = (l + r) // 2
    if can(mid, k):
        l = mid
    else:
        r = mid
# print(can(l, k), can(r, k))
print(l)
