t = int(input())

def f(n):
    if n < 10:
        return n
    tmp = n - ((n // 10) * 10)
    return (n - tmp) + f(tmp + (n - tmp)//10)

for i in range(t):
    s = int(input())
    print(f(s))