a, b, c = map(int, input().split())

areas = []
areas.append((a % 2) * b * c)
areas.append(a * (b % 2) * c)
areas.append(a * b * (c % 2))

print(min(areas))
