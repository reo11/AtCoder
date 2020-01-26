from collections import Counter
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    a = Counter(a)
    return a

t = int(input())
for i in range(t):
    n = int(input())
    a = prime_factorize(n)
    flag = True
    ans = ""

    if len(a.keys()) == 1:
        for k, v in a.items():
            if v <= 5:
                flag = False
            else:
                ans = "{} {} {}".format(k, k**2, k**(v-3))
    elif len(a.keys()) == 2:
        v_pair = []
        vk_pair = []
        for k, v in a.items():
            v_pair.append(v)
            vk_pair.append((v, k))

        if max(v_pair) >= 3 or (v_pair[0] >= 2 and v_pair[1] >= 2):
            ans = "{} {} {}".format(
                vk_pair[0][1], vk_pair[1][1], vk_pair[0][1] ** (vk_pair[0][0] - 1) * vk_pair[1][1] ** (vk_pair[1][0] - 1))
        else:
            flag = False
    else:
        b = 1
        for j, (k, v) in enumerate(a.items()):
            if j <= 1:
                ans += "{} ".format(str(k ** v))
            else:
                b *= k ** v
        ans += "{}".format(b)

    if flag:
        print("YES")
        print(ans)
    else:
        print("NO")
