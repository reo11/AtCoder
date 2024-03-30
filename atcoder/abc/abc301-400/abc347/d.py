from itertools import combinations

a, b, c = map(int, input().split())
used_c_bits = []
for i in range(60):
    if c & (1 << i):
        used_c_bits.append(i)

bits_to_delete = (a + b) - len(used_c_bits)
if bits_to_delete < 0:
    # aとbでは足りない
    print(-1)
    exit()
if bits_to_delete % 2 == 1:
    # xorでは無理
    print(-1)
    exit()

# 他の場合は可能なはず？
used_a = a
used_b = b
used_a -= bits_to_delete // 2
used_b -= bits_to_delete // 2

if used_a < 0 or used_b < 0:
    print(-1)
    exit()

a_candidates = used_c_bits[:used_a]

a_num = 0
for i in a_candidates:
    a_num += 1 << i

b_num = c ^ a_num
b_candidates = []
for i in range(60):
    if b_num & (1 << i):
        b_candidates.append(i)

def count_bit(n):
    cnt = 0
    while n > 0:
        cnt += n & 1
        n >>= 1
    return cnt
a_candidates = set(a_candidates)
b_candidates = set(b_candidates)

bit_to_add = []
count = 0
# print(a_candidates, b_candidates)
if bits_to_delete > 0:
    for i in range(60):
        if i not in a_candidates and i not in b_candidates:
            bit_to_add.append(i)
            count += 1
            if count >= (bits_to_delete // 2):
                break

for i in bit_to_add:
    a_num += 1 << i
    b_num += 1 << i
# print(a_num, b_num)
# # print(a_candidates)
# print(a_num, b_num, count_bit(a_num), count_bit(b_num))
# print(a_num ^ b_num)
if count_bit(a_num) != a or count_bit(b_num) != b:
    print(-1)
else:
    print(a_num, b_num)
