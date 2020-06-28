n = int(input())
s = str(input())

ans_s = s
ans_head = 0
ans_tail = 0

def remove(s):
    while True:
        if len(s) <= 0:
            break
        pre_len = len(s)
        s = s.replace("()", "")
        if len(s) == pre_len:
            break
    return s

s = remove(s)
while len(s) > 0:
    s = remove(s)
    if s[0] == ')':
        ans_head += 1
        s = remove('(' + s)
    else:
        ans_tail += 1
        s = remove(s + ')')
    # print(s)
print('('*ans_head + ans_s + ')' * ans_tail)

