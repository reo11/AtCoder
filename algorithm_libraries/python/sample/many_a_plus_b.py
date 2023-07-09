def a_plus_b(a, b):
    return a + b

if __name__ == "__main__":
    t = int(input())
    ans = []
    for _ in range(t):
        a, b = map(int, input().split())
        ans.append(a_plus_b(a, b))
    print(*ans, sep='\n')