def a_plus_b(a, b):
    return a + b

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(a_plus_b(a, b))