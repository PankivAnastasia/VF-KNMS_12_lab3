def encode_cezar(text):
    letters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text:
        if letter in letters:
            index = letters.index(letter)
            abc_len = len(letters)
            new_index = index + 1
            if new_index > abc_len:
                new_index = new_index - abc_len
            result = result + letters[new_index]
        else:
            result = result + letter

    return result

