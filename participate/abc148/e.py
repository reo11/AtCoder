n = int(input())

def f(num):
    num = num - int(str(num)[-1])
    count = 0
    i = 1
    while True:
        if ((5 ** i) * (2)) > num:
            break
        count += (num // ((5 ** i) * (2)))
        i += 1
    return count


# 偶数 => 出てくる5の個数
# 奇数 => 0
if n % 2 == 1:
    print(0)
    exit()
else:
    print(f(n))