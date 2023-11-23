s = input()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in range(5):
    if s == days[i]:
        print(5 - i)
        exit()