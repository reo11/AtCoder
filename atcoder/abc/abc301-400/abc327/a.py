n = int(input())
s = input()

for i in range(1, n):
    if set([s[i - 1], s[i]]) == set(["a", "b"]):
        print("Yes")
        exit()
print("No")
