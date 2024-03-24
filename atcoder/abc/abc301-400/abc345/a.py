s = list(input())

if s[0] == "<" and s[-1] == ">" and set(s[1:-1]) == set(["="]):
    print("Yes")
else:
    print("No")