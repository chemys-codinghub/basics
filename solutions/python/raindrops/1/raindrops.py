def convert(number):
    message = ""
    if not number % 3:
        message += "Pling"
    if not number % 5:
        message += "Plang"
    if not number % 7:
        message += "Plong"
    if not message:
        message += str(number)

    return message
