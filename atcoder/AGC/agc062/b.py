n, k = map(int, input().split())
c = list(map(int, input().split()))
p = list(map(int, input().split()))


def count_seq(A):
    min_a = float("inf")
    count = 0
    for a_i in A:
        if min_a > a_i:
            count += 1
            min_a = min(min_a, a_i)
    return count - 1


print(count_seq(p))
