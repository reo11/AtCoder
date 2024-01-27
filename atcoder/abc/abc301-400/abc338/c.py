n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def solve(q, x):
    # 材料qでxを作れる最大数
    ans = []
    for qi, xi in zip(q, x):
        if xi == 0:
            continue
        ans.append(qi // xi)
    return min(ans)

# 全探索
ans = 0
max_a = solve(q, a)
for i in range(0, max_a + 1):
    q_tmp = [qi - i * xi for qi, xi in zip(q, a)]
    max_b = solve(q_tmp, b)
    ans = max(ans, i + max_b)
print(ans)

