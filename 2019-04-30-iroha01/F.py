import math
import collections
def trial_division_sqrt(n):
    prime_count = collections.Counter()

    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[n] += 1

    return prime_count

n, k = map(int, input().split())
counter = trial_division_sqrt(n)
counter = sorted(counter.items())
ans_list = []
for (key, value) in counter:
    for i in range(value):
        ans_list.append(int(key))


if len(ans_list) < k:
    print(-1)
elif len(ans_list) == k:
    ans = str(ans_list[0])
    for i in ans_list[1:]:
        ans += " " + str(i)
    print(ans)
else:
    new_ans_list = []
    for i in range(k - 1):
        new_ans_list.append(ans_list[i])
    multi = 1
    for v in ans_list[k-1:]:
        multi *= v
    new_ans_list.append(multi)
    ans = str(new_ans_list[0])
    for i in new_ans_list[1:]:
        ans += " " + str(i)
    print(ans)
