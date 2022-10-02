goal, wall, hammer = map(int, input().split())

if 0 <= wall and wall <= goal:
    if hammer <= wall:
        print(abs(hammer) + abs(goal - hammer))
    else:
        print(-1)
elif goal <= wall and wall <= 0:
    if wall <= hammer:
        print(abs(hammer) + abs(goal - hammer))
    else:
        print(-1)
else:
    print(abs(goal))