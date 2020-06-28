from math import sqrt, cos, radians
a, b, h, m = map(int, input().split())

def yogen(b, c, shi):
    return sqrt(b**2+c**2 - 2*b*c*cos(shi))

shi1 = radians(m / 60 * 360)
shi2 = radians((h * 60 + m)/(12*60)*360)

print(yogen(a, b, abs(shi1 - shi2)))
