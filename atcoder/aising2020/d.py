n = int(input())
x = input()
COUNT = x.count("1")
mod1 = COUNT - 1
mod2 = COUNT + 1

# その桁に1が立っていた時の余り
mod = [[0, 0] for _ in range(n + 1)]
mult = 1
if mod1 != 0:
    mod[0][0] = 1 % mod1
mod[0][1] = 1 % mod2
for i in range(1, n + 1):
    if mod1 != 0:
        mod[i][0] = (mod[i - 1][0] * (2 % mod1)) % mod1
    mod[i][1] = (mod[i - 1][1] * (2 % mod2)) % mod2

all_mod1 = 0
all_mod2 = 0
for i in range(n):
    if x[i] == "1":
        if mod1 != 0:
            all_mod1 = all_mod1 + mod[n - 1 - i][0]
        all_mod2 = all_mod2 + mod[n - 1 - i][1]
if mod1 != 0:
    all_mod1 %= mod1
all_mod2 %= mod2


def popcount(idx):
    idx -= 1
    ret = 0
    if x[idx] == "1":
        if mod1 != 0:
            ret = (all_mod1 - mod[n - 1 - idx][0]) % mod1
        else:
            ret = -1
    else:
        ret = (all_mod2 + mod[n - 1 - idx][1]) % mod2
    return ret


bit_cnt_table = [0 for _ in range(n + 1)]
bit_cnt_table[1] = 1
base = 0
i = 2
while i <= n:
    if i % (2**base) == 0:
        base += 1
    bit_cnt_table[i] = 1 + bit_cnt_table[i - 2 ** (base)]
    i += 1


def func(num):
    if bit_cnt_table[num] == 0:
        return 0
    return num % bit_cnt_table[num]


f = [-1 for _ in range(n + 1)]
f[0] = 0
f[1] = 1
for i in range(2, n + 1):
    tmp = func(i)
    f[i] = 1 + f[tmp]
# print("all_mod", all_mod1, all_mod2)
ans = []
for i in range(1, n + 1):
    p = popcount(i)
    if p == -1:
        ans_i = 0
    else:
        ans_i = 1 + f[p]
    # print(i, p, ans_i)
    ans.append(str(ans_i))
print("\n".join(ans))
# print(f)
# print(bit_cnt_table)
