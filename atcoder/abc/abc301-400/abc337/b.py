s = list(input())

flatten = []
for i, si in enumerate(s):
    if i == 0:
        flatten.append(si)
    else:
        if flatten[-1] == si:
            continue
        else:
            flatten.append(si)
flatten = "".join(flatten)
if flatten in ["A", "AB", "ABC", "B", "BC", "C", "AC"]:
    print("Yes")
else:
    print("No")