letters = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: "h", 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
    21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}
move_length = 13


def __find_letter_index(lett):
    for ind, letter in letters.items():
        if letter == lett:
            return ind

    return 0


def __rotate_character(lett):
    inx = __find_letter_index(lett.lower())
    if inx == 0:
        return lett

    if inx > move_length:
        new_ind = inx - move_length
    else:
        new_ind = inx + move_length

    return letters[new_ind] if lett.isupper() is False else letters[new_ind].upper()


def __transform_text(text):
    list_of_chars = list(text)
    output_chars = []

    for let in list_of_chars:
        new_char = __rotate_character(let)
        output_chars.append(new_char)

    return ''.join(output_chars)


def decrypt(encrypted_text):
    return __transform_text(encrypted_text)


def encrypt(text_to_encrypt):
    return __transform_text(text_to_encrypt)
