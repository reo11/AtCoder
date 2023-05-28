from collections import defaultdict
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
            ans = set()
            # 外側
            for i in range(1, n + 1):
                if i == n:
                    ans.add(f"1 {i}")
                else:
                    ans.add(f"{i} {i + 1}")
                if len(ans) >= n * d:
                    break
            # 対角線
            for skip_dist in range(2, n):
                # print(skip_dist, len(ans))
                visited = set()
                start_i = 1
                while len(visited) < n:
                    while start_i in visited:
                        start_i += 1
                        if start_i > n:
                            start_i -= n
                    end_i = start_i + skip_dist
                    if end_i > n:
                        end_i -= n
                    # print(start_i, end_i)
                    ans_i = [start_i, end_i]
                    ans_i.sort()
                    ans_i = f"{ans_i[0]} {ans_i[1]}"
                    if ans_i not in ans:
                        ans.add(ans_i)
                    visited.add(start_i)
                    # 次の準備
                    start_i += end_i + skip_dist
                    if start_i > n:
                        start_i -= n
                    if len(ans) >= n * d:
                        break
                if len(ans) >= n * d:
                    break
            return list(ans)[:n*d]
        else:
            return []
def count_number_in_ans(ans):
    c = defaultdict(int)
    for s in ans:
        num1, num2 = map(int, s.split())
        c[num1] += 1
        c[num2] += 1
    return c

ans = solve(n, d)
# print(ans)
if len(ans) == 0:
    ans = ["No"]
else:
    ans.sort()
    # print(count_number_in_ans(ans))
    ans = ["Yes"] + ans
print(*ans, sep='\n')