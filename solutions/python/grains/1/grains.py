def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    sum_grains = 0
    for n in range(64):
        sum_grains += square(n + 1)
    return sum_grains
