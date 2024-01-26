from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

q = int(input())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

all_newest = [0, -1]
a_sum = defaultdict(lambda: 0)

for i in range(n):
    a_sum[i] = a[i]


for t in range(q):
    query = queries[t]
    query_type = query[0]
    if query_type == 1:
        x = query[1]
        all_newest = [t, x]
        a_sum = defaultdict(lambda: 0)
    elif query_type == 2:
        i = query[1] - 1
        x = query[2]
        a_sum[i] += x
    else:
        i = query[1] - 1
        ans = 0
        if all_newest[1] != -1:
            ans += all_newest[1]
        print(ans + a_sum[i])
