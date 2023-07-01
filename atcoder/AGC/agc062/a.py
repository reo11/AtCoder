t = int(input())


def f(t):
    a_idx = []
    b_idx = []
    for i in range(len(t) - 1):
        if t[i] == "A":
            a_idx.append(i)
        else:
            b_idx.append(i)
    ret = []
    for i in a_idx:
        ret.append(t[i + 1])
    for i in b_idx:
        ret.append(t[i + 1])
    return "".join(ret)


def solve1(s):
    t = f(s)
    # print(t)
    while len(t) > 1:
        t = f(t)
        # print(t)
    return t


def solve2(s):
    # AとBが連続している場合まとめる
    def squeeze(s):
        tmp = [""]
        for i in range(len(s)):
            if tmp[-1] != s[i]:
                tmp.append(s[i])
        return "".join(tmp)

    t = squeeze(s)
    while len(t) > 1:
        t = f(t)
        t = squeeze(t)
        # print(t)
    return t


ans = []
for _ in range(t):
    n = int(input())
    s = input()
    # ans.append(solve1(s))
    ans.append(solve2(s))
print(*ans, sep="\n")
