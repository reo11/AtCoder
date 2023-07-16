import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

# 次の遷移を決める
def dfs(past_set, last_str):
    ret = False
    # print(past_set, last_str)

    for next_num in range(n):
        if next_num in past_set:
            continue
        next_str = s[next_num]
        cost = 0
        for i in range(m):
            if next_str[i] != last_str[i]:
                cost += 1
            if cost > 1:
                break
        if cost > 1:
            continue
        if len(past_set) == n - 1:
            return True
        else:
            ret |= dfs(past_set | {next_num}, next_str)
    return ret


ans = False

for i in range(n):
    ans |= dfs({i}, s[i])
    # print(i, ans)

print(["No", "Yes"][ans])
