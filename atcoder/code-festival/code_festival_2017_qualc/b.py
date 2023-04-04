n = int(input())
a = list(map(int, input().split()))

count_all = 1
count_even = 1
for i in range(n):
    a_i = a[i]
    count_all *= 3
    if a_i % 2 == 0:
        count_even *= 2
print(count_all - count_even)
