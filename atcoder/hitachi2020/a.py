s = str(input().rstrip())
if s in ["hi" * x for x in range(1, 6)]:
    print("Yes")
else:
    print("No")
