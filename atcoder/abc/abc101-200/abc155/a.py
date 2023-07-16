a = list(map(int, input().split()))
a_set = len(set(a))

if a_set == 2:
    print("Yes")
else:
    print("No")
