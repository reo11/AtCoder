import bisect


def bin_search_list(a, min_v, max_v):
    # a is sorted
    left = bisect.bisect_left(a, min_v)
    right = bisect.bisect_left(a, max_v)
    size = right - left + 1
    return left, right, size


n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for i in range(n):
    for j in range(i+1, n):
        a = l[i]
        b = l[j]
        left, right, size = bin_search_list(l, max(a-b, b-a)+1, a+b-1)
        tmp = size
        if right >= n:
            tmp -= 1
        for k in [i, j]:
            if left <= k <= right:
                tmp -= 1
        ans = ans + max(tmp, 0)
print(ans//3)

