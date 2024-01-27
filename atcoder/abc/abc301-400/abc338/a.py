s = list(input())

flag = True
big_alphabet = set([chr(ord("A") + i) for i in range(26)])
small_alphabet = set([chr(ord("a") + i) for i in range(26)])

if s[0] not in big_alphabet:
    flag = False

for i in range(1, len(s)):
    if s[i] not in small_alphabet:
        flag = False

if flag:
    print("Yes")
else:
    print("No")