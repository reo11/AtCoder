from typing import Iterator, List, Set


def bit_full_search(max_bit: int) -> Iterator[List[int]]:
    for i in range(2 ** max_bit):
        bit_list = [0 for _ in range(max_bit)]
        for j in range(max_bit):
            if i & (2 ** j) > 0:
                bit_list[max_bit - j - 1] = 1
        yield bit_list

def solve(s: List[Set[str]]):
    ans = 0

    for i in range(26):
        target_c = chr(ord("a") + i)
        count = 0
        for batch_s in s:
            if target_c in batch_s:
                count += 1
        if count == k:
            ans += 1
    return ans

n, k = map(int, input().split())
s = []
ans = 0
for _ in range(n):
    s.append(set(list(input())))

for l in bit_full_search(n):
    batch_s = []
    for i in range(n):
        if l[i]:
            batch_s.append(s[i])
    # print(l, batch_s)
    ans = max(ans, solve(batch_s))

print(ans)


