def is_armstrong_number(number):
    num_str = str(number)
    expo = len(num_str)

    total = sum(int(digit) ** expo for digit in num_str)
    return number == total
