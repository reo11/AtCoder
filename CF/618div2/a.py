t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cost = 0
    num_zero = a.count(0)
    sum_a = sum(a)
    if num_zero > 0:
        cost += num_zero
        sum_a += num_zero
    if sum_a == 0:
        cost += 1
    print(cost)