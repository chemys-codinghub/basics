def is_armstrong_number(number):
    num_str = str(number)
    pow = len(num_str)

    total = sum(int(digit) ** pow for digit in num_str)
    return number == total
