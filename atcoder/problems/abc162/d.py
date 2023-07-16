from collections import defaultdict

n = int(input())
s = list(input())

cnts = defaultdict(lambda: 0)
for i in range(n):
    cnts[s[i]] += 1
# 全パターン数える
ans = cnts["R"] * cnts["G"] * cnts["B"]

# 条件2を満たさないものを引く
for left in range(n):
    for mid in range(left + 1, n):
        right = mid + abs(mid - left)
        if right >= n:
            # nを超える場合はスキップ
            continue
        # 3文字全てが異なる場合を集合で判定して除外する
        if len(set([s[left], s[mid], s[right]])) == 3:
            ans -= 1
print(ans)
