from typing import Iterator, List


def bit_full_search(max_bit: int) -> Iterator[List[int]]:
    for i in range(2 ** max_bit):
        bit_list = [0 for _ in range(max_bit)]
        for j in range(10):
            if i & 2 ** j > 0:
                bit_list[j] = 1
        yield bit_list



n = int(input())

f = []
for i in range(n):
    f.append(list(map(int, input().split())))

p = []
for i in range(n):
    p.append(list(map(int, input().split())))

# bit全探索
ans = -(10 ** 10)

for l in bit_full_search(10):
    if sum(l) == 0:
        continue
    score = 0
    for j in range(n):
        count = 0
        for k in range(10):
            if f[j][k] == l[k] == 1:
                count += 1
        score += p[j][count]
    ans = max(ans, score)
print(ans)
