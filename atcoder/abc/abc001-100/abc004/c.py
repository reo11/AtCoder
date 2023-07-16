n = int(input())
card = list(range(1, 7))
for i in range(n % 30):
    idx = i % 5
    tmp = card[idx]
    card[idx] = card[idx + 1]
    card[idx + 1] = tmp
card = list(map(str, card))
print("".join(card))
