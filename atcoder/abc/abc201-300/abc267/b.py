s = list(map(int, list(input())))

flags = [1 for _ in range(7)]

if s[6] == 0:
    flags[0] = 0

if s[3] == 0:
    flags[1] = 0

if s[1] == 0 and s[7] == 0:
    flags[2] = 0

if s[0] == 0 and s[4] == 0:
    flags[3] = 0

if s[2] == 0 and s[8] == 0:
    flags[4] = 0

if s[5] == 0:
    flags[5] = 0

if s[9] == 0:
    flags[6] = 0

if s[0] == 1:
    print("No")
    exit()

for left in range(5):
    for mid in range(left + 1, 6):
        for right in range(mid + 1, 7):
            if flags[left] == 1 and flags[mid] == 0 and flags[right] == 1:
                print("Yes")
                exit()
print("No")
