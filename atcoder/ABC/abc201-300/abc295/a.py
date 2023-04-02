n = int(input())
w = list(input().split())

targets = ["and", "not", "that", "the", "you"]
count = 0
for word in w:
    if word in targets:
        count += 1
if count > 0:
    print("Yes")
else:
    print("No")
