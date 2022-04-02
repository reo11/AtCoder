import itertools
from collections import defaultdict

n, m = map(int, input().split())
connected_dict = defaultdict(lambda: [])

for i in range(m):
    a, b = map(int, input().split())
    connected_dict[a].append(b)
    connected_dict[b].append(a)

count = 0
for permutation in list(itertools.permutations(range(2, n + 1))):
    flag = True
    pre_num = 1
    for num in permutation:
        if num not in connected_dict[pre_num]:
            flag = False
            break
        pre_num = num
    if flag:
        count += 1
print(count)
