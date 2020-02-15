s = input().rstrip()
s_len = len(s)
if s_len == 2:
    print(s)
else:
    print("".join(list(s[::-1])))