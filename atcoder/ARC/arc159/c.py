import time
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))


def process(d):
    if len(d) > 2:
        # [current_value, init_index, add_list]
        sorted_d = sorted(d)
        sorted_d = [sorted_d[-1]] + sorted_d[:-1]
        for i, num in enumerate(range(1, n + 1)):
            sorted_d[i][2].append(num)
        n_list = [i for i in reversed(range(1, n + 1))]
        n_list[0] = n - 1
        n_list[1] = n
        for i, num in enumerate(n_list):
            sorted_d[i][2].append(num)

        sorted_d[0][0] -= 1
        sorted_d[1][0] += 1
        return sorted_d, 2
    else:
        sorted_d = sorted(d)
        sorted_d[0][0] += 1
        sorted_d[0][2].append(2)
        sorted_d[1][2].append(1)
        return sorted_d, 1


def solve():
    s = sum(a)
    ans_list = []

    if (s + (n * (1 + n) // 2)) % n == 0 or s % n == 0:
        if (s + (n * (1 + n) // 2)) % n == 0:
            for i in range(n):
                ans_list.append([a[i] + i + 1, i, [i + 1]])
            ans = 1
        else:
            for i in range(n):
                ans_list.append([a[i], i, []])
            ans = 0
        while True:
            set_a = set([x[0] for x in ans_list])
            if len(set_a) == 1:
                break
            ans_list, count = process(ans_list)
            ans += count
            # print(ans, ans_list)
            # time.sleep(0.5)
            if ans > 10000:
                print("No")
                return
        print("Yes")
        print(len(ans_list[0][-1]))
        ans_list = sorted(ans_list, key=lambda x: x[1])
        ans_print = [[] for _ in range(len(ans_list[0][-1]))]
        for i in range(len(ans_list[0][-1])):
            for j in range(n):
                ans_print[i].append(ans_list[j][2][i])
        ans_print_all = []
        for l in ans_print:
            ans_print_all.append(" ".join(list(map(str, list(map(int, l))))))
        if len(ans_print_all) > 0:
            print("\n".join(ans_print_all))
    else:
        print("No")


solve()
