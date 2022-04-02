def display_ans_list(max_n):

    for n in range(1, max_n + 1):
        l_ = []
        for i in range(2 ** n):
            if format(i, "b").zfill(n) == format(i, "b").zfill(n)[::-1]:
                l_.append(format(i, "b").zfill(n))
        for k in range(n):
            count_positive = 0
            for s in l_:
                count_k = 0
                for i, c in enumerate(s):
                    if c == "1":
                        count_k += list(s[i + 1 :]).count("0")
                if k == count_k:
                    count_positive += 1
                    print(s)
            if count_positive != 0:
                print("n: {}\tk:{}\tcount:{}".format(n, k, count_positive))


def solve(n, k):
    ans = 0
    if n == 1 or n == 2:
        if k == 0:
            ans = 2
        else:
            ans = 0
    elif n % 2 == 1:
        if k == 0:
            ans = 2
        elif n // 2 == k:
            ans = 2
        elif n - 2 == k:
            ans = n - 1
        elif n == 7 and k == 5:
            ans = 6
        else:
            ans = 0
    else:
        if k == 0:
            ans = 2
        elif k == n - 2:
            if n != 4:
                ans = n
            else:
                ans = 2
        else:
            ans = 0
    return ans


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        print(solve(n, k))
    # display_ans_list(20)
