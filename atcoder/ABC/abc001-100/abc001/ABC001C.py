from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal

deg, dis = map(int, input().split())
direction = []
name = [
    "N",
    "NNE",
    "NE",
    "ENE",
    "E",
    "ESE",
    "SE",
    "SSE",
    "S",
    "SSW",
    "SW",
    "WSW",
    "W",
    "WNW",
    "NW",
    "NNW",
    "N",
]
d = -11.25
i = 0
while True:
    direction.append([d, d + 22.5, name[i]])
    i += 1
    d += 22.5
    if i == len(name):
        break

wind = [
    "0.0",
    "0.3",
    "1.6",
    "3.4",
    "5.5",
    "8.0",
    "10.8",
    "13.9",
    "17.2",
    "20.8",
    "24.5",
    "28.5",
    "32.7",
]
wind = list(map(float, wind))

ans_d = None
ans_w = 12
for min_, max_, name in direction:
    if min_ <= deg / 10 < max_:
        ans_d = name
        break

for i in range(len(wind) - 1):
    d_ = dis / 60
    d_ = Decimal(str(d_)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

    if wind[i] <= float(d_) + 0.00001 < wind[i + 1]:
        ans_w = i
        break
if ans_w == 0:
    ans_d = "C"
print(ans_d, ans_w)
