def base10int(num_10, n):
    str_n = []
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n.append(num_10 % n)
        num_10 //= n
    return str_n[::-1]


def solve():
    n, k = map(int, input().split())
    three = base10int(n, 3)
    # print(three)
    count = sum(three)
    # countは最小の分解数
    if count > k:
        # countは増やせるが、減らせないのでkを超えている場合はFalse
        return False
    # 3 ** k = 3 ** (k - 1) * 3 で1つを3つにできる、つまり2つずつ増やせる
    # nまで分解可能であるため、kとcountの差が2の倍数で、kがn以下ならちょうどk個で表現可能
    if (k - count) % 2 == 0:
        return True
    else:
        return False


t = int(input())
ans = []

for _ in range(t):
    if solve():
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep="\n")
