# ABC123
def pro_a():
    a = []
    for i in range(5):
        a.append(int(input()))
    k = int(input())
    ans = True
    for i in range(5):
        for j in range(5):
            if abs(a[i] - a[j]) > k:
                ans = False
    if ans:
        print('Yay!')
    else:
        print(':(')

def pro_b():
    import math
    a = [[0]*3 for i in range(5)]
    min_inp = 0
    for i in range(5):
        inp = int(input())
        inp_ceil = math.ceil(inp/10)
        first = inp - int(inp/10) * 10
        a[i][0].append(inp)
        a[i][1].append(inp_ceil)
        a[i][2].append(first)
    print(a)
    # ans = sum(a)
    print(ans)


def pro_c():
    a = input()
    print(a)

def pro_d():
    a = input()
    print(a)

if __name__ == '__main__':
    pro_b()
