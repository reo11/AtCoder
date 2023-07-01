def sort(a):
    return sorted(a)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    print(" ".join(map(str, sort(a))))
