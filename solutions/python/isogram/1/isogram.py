def is_isogram(string):
    string = string.lower()
    clean_string = "".join(char for char in string if char.isalpha())
    return len(set(clean_string)) == len(clean_string)
