import sys
input = lambda: sys.stdin.readline().rstrip()

s = list(input())
words = []
word = [s[0]]
during_word = True
for c in s[1:]:
    is_up = c.isupper()
    word.append(c)
    if is_up:
        if during_word:
            word = "".join(word)
            words.append(word.lower())
            during_word = False
            word = []
        else:
            during_word = True

words.sort()
ans = []
for word in words:
    m = len(word)
    ans.append(word[0].upper() + word[1:m-1] + word[m-1].upper())
print("".join(ans))