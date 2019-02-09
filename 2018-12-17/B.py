# -*- coding: utf-8 -*-

N, Q = map(int, input().split())
sort_list = [chr(ord('A') + i) for i in range(N)]
new_list = sort_list

if N == 26:
    end = False
    count = 0
    while end == False:
        for i in range(25):
            for j in range(25):
                if i < j:
                    print("? {} {}".format(new_list[i], new_list[j]))
                    answer = input()
                    # < or >
                    if answer == ">":
                        new_list[i], new_list[j] = new_list[j], new_list[i]
                    else:
                        count += 1
        if count >= 300:
            end = True

if N == 5:
    a = 0
    b = 1
    print("? {} {}".format(new_list[a], new_list[b]))
    answer = input()
    # < or >
    if answer == ">":
        new_list[a], new_list[b], new_list[4] = new_list[b], new_list[4], new_list[a]
    else:
        new_list[b], new_list[4] = new_list[4], new_list[b]
    a = 1
    b = 3
    print("? {} {}".format(new_list[a], new_list[b]))
    answer = input()
    if answer == ">":
        new_list[a], new_list[b] = new_list[b], new_list[a]

    a = 0
    b = 1
    print("? {} {}".format(new_list[a], new_list[b]))
    answer = input()
    # < or >
    if answer == ">":
        new_list[a], new_list[b] = new_list[b], new_list[a]

    a = 3
    b = 4
    print("? {} {}".format(new_list[a], new_list[b]))
    answer = input()
    # < or >
    if answer == ">":
        new_list[a], new_list[b] = new_list[b], new_list[a]

    a = 2
    b = 1
    print("? {} {}".format(new_list[a], new_list[b]))
    answer = input()
    if answer == "<":
        b = 3
        print("? {} {}".format(new_list[a], new_list[b]))
        answer = input()
        if answer == ">":
            new_list[a], new_list[b] = new_list[b], new_list[a]
            a = b
            b = 4
            print("? {} {}".format(new_list[a], new_list[b]))
            answer = input()
            if answer == ">":
                new_list[a], new_list[b] = new_list[b], new_list[a]
        else:
            print("? {} {}".format(new_list[1], new_list[3]))
            answer = input()
            if answer == ">":
                new_list[1], new_list[3] = new_list[3], new_list[1]
    else:
        new_list[a], new_list[b] = new_list[b], new_list[a]
        a = b
        b = 0
        print("? {} {}".format(new_list[a], new_list[b]))
        answer = input()
        if answer == ">":
            new_list[a], new_list[b] = new_list[b], new_list[a]
            print("? {} {}".format(new_list[2], new_list[3]))
            answer = input()
            if answer == ">":
                new_list[2], new_list[3] = new_list[3], new_list[2]
        else:
            print("? {} {}".format(new_list[2], new_list[3]))
            answer = input()
            if answer == ">":
                new_list[2], new_list[3] = new_list[3], new_list[2]

print("! " + "".join(new_list))
