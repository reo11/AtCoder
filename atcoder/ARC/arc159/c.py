from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

ans_list = []
for i in range(n):
    ans_list.append([a[i], i, []])

ans = -1
for count in range(10002):
    set_a = set([x[0] for x in ans_list])
    if len(set_a) == 1:
        ans = count
        break
    tmp_ans_list = []
    for i, (a_j, j, l) in enumerate(sorted(ans_list, reverse=True), start=1):
        tmp_ans_list.append([a_j + i, j, l + [i]])
    ans_list = tmp_ans_list

if ans == -1:
    print("No")
else:
    print("Yes")
    print(ans)
    ans_list = sorted(ans_list, key=lambda x: x[1])
    ans_print = [[] for _ in range(ans)]
    for i in range(ans):
        for j in range(n):
            ans_print[i].append(ans_list[j][2][i])
    ans_print_all = []
    for l in ans_print:
        ans_print_all.append(" ".join(list(map(str, list(map(int, l))))))
    if len(ans_print_all) > 0:
        print("\n".join(ans_print_all))