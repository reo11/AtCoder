abc = input()
abc_sets = set()

for i in range(1, 350):
    if i == 316:
        continue
    num_str = str(i)
    num_str = "0" * (3 - len(num_str)) + num_str
    abc_sets.add("ABC" + num_str)

if abc in abc_sets:
    print("Yes")
else:
    print("No")