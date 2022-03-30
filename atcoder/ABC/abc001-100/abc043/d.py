s = list(map(lambda x: ord(x) - ord('a'), list(input())))

ans = ["-1", "-1"]
# print(s)
if len(s) == 2:
    if len(set(s)) == 1:
        print(1, 2)
        exit()
    else:
        print(" ".join(ans))
        exit()

for i in range(len(s) - 2):
    # print(len(set(s[i:i+3])))
    if len(set(s[i:i+3])) <= 2:
        # print(s[i:i+3])
        ans = [str(i+1), str(i+3)]
        break

print(" ".join(ans))