n, d = map(int, input().split())


def solve(n, d):
    if n <= 1:
        # 1頂点しかない場合は不可能
        return []
    elif n == 2:
        # 2頂点の場合は、d次第
        if d <= 0:
            return ["1 2"]
        else:
            return []
    else:
        max_nd = n + n * (n - 3) // 2
        if n * d <= max_nd:
            ans = []
            # 外側
            for i in range(1, n):
                if i == n:
                    ans.append(f"1 {i}")
                else:
                    ans.append(f"{i} {i + 1}")
                if len(ans) == n * d:
                    break
            # 対角線
            for skip_dist in range(2, n):
                for start_i in range(1, n - skip_dist + 1):
                    ans.append("{} {}".format(start_i, start_i + skip_dist))
                    if len(ans) == n * d:
                        break
                if len(ans) == n * d:
                    break
            return ans
        else:
            return []


ans = solve(n, d)
# print(ans)
if len(ans) == 0:
    ans = ["No"]
else:
    ans.sort()
    ans = ["Yes"] + ans
print(*ans, sep="\n")
