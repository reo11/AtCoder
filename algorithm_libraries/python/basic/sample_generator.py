import random

MIN0 = 0
MIN5 = -(10**5)
MIN9 = -(10**9)
MAX5 = 10**5
MAX9 = 10**9
MAX18 = 10**18


def int_generator(min_value: int = MIN0, max_value: int = MAX5) -> int:
    return random.randint(min_value, max_value)


def pair_generator(
    x_min: int = MIN0, x_max: int = MAX5, y_min: int = MIN0, y_max: int = MAX5
) -> tuple:
    return (int_generator(x_min, x_max), int_generator(y_min, y_max))


if __name__ == "__main__":
    f = open("sample.txt", "w", encoding="UTF-8")
    datalist = []
    n = int_generator(1, 5 * 10**5)
    k = int_generator(1, n)
    q = int_generator(1, 5 * 10**5)
    datalist.append(f"{n} {k} {q}\n")
    for _ in [0] * q:
        x, y = pair_generator(1, n, 0, MAX9)
        datalist.append(f"{x} {y}\n")
    f.writelines(datalist)
    f.close()
