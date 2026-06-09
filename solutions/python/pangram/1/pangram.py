def is_pangram(sentence):
    set_text = set(sentence.lower())
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set_text)
