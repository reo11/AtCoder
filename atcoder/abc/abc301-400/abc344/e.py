from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = []

# 連想配列を実装する
# 一つ前と一つあとの数字を持つ
# 先頭は-1, 最後は-1
# 自分自身の数字をキーとしたdict
# {1: [-1, 2], 2: [1, 3], 3: [2, 4], 4: [3, -1]}

chain_array = defaultdict(lambda: [-1, -1])

for i in range(len(a)):
    if i > 0:
        chain_array[a[i]][0] = a[i-1]
    if i < len(a)-1:
        chain_array[a[i]][1] = a[i+1]

for _ in range(q):
    query_type, *query = map(int, input().split())
    if query_type == 1:
        # xの後ろにyを挿入
        x, y = query
        tmp_next = chain_array[x][1]
        if tmp_next != -1:
            chain_array[tmp_next][0] = y
        chain_array[x][1] = y
        chain_array[y] = [x, tmp_next]
    else:
        # xを削除
        x = query[0]
        tmp_prev = chain_array[x][0]
        tmp_next = chain_array[x][1]
        if tmp_prev != -1:
            chain_array[tmp_prev][1] = tmp_next
        if tmp_next != -1:
            chain_array[tmp_next][0] = tmp_prev
        chain_array.pop(x)

num = -1
for k, v in chain_array.items():
    if v[0] == -1:
        num = k
        break

ans = []
while num != -1:
    ans.append(num)
    num = chain_array[num][1]

print(*ans, sep=" ")