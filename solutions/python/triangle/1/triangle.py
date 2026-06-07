def is_valid(sides):
    a, b, c = sides
    return a + b > c and b + c > a and c + a > b

def equilateral(sides):
    a, b, c = sides
    if not is_valid(sides):
        return False
    return a == b == c


def isosceles(sides):
    a, b, c = sides
    if not is_valid(sides):
        return False
    return a == b or b == c or c == a


def scalene(sides):
    a, b, c = sides
    if not is_valid(sides):
        return False
    return not equilateral(sides) and not isosceles(sides)
