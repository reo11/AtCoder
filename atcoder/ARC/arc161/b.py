import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())


def solve(n):
    ans = []
    while True:
        if n < 3:
            ans = -1
            break
        bin_list = list(str(bin(n)).replace("0b", ""))
        # 上位ビットはできるだけ残す
        one_count = bin_list.count("1")
        if one_count >= 3:
            # 3以上の場合は、上位ビットを残す
            count = 0
            for i in range(len(bin_list)):
                if count < 3 and bin_list[i] == "1":
                    count += 1
                    ans.append("1")
                else:
                    ans.append("0")
            ans = int("".join(ans), 2)
            break
        else:
            n -= 1
    return ans


ans = []
for _ in range(t):
    n = int(input())
    ans.append(solve(n))
print(*ans, sep="\n")
