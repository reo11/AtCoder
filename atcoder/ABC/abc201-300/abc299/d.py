n = int(input())


def question(i):
    print(f"? {i}")
    return int(input())


def answer(i):
    print(f"! {i}")


def solve():
    left = 0
    right = n
    mid = (left + right) // 2

    q_count = 0
    while q_count <= 20:
        if left + 1 == right:
            break
        next_num = question(mid)
        if next_num == 1:
            right = mid
        else:
            left = mid
        mid = (left + right) // 2
    return left


answer(solve())
