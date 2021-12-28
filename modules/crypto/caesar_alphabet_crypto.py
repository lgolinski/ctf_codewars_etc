letters = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: "h", 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
    21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}
move_length = 0
let_length = len(letters)


def __find_letter_index(lett):
    for ind, letter in letters.items():
        if letter == lett:
            return ind

    return 0


def __find_new_index(act_inx):
    new_move = act_inx + move_length
    increment = int(new_move / let_length)
    if increment == 0:
        return new_move

    ret = new_move - (increment * let_length)

    if ret == 0:
        return list(letters.keys())[-1]

    return ret


def __rotate_character(lett):
    inx = __find_letter_index(lett.lower())
    if inx == 0:
        return lett

    new_ind = __find_new_index(inx)

    return letters[new_ind] if lett.isupper() is False else letters[new_ind].upper()


def __transform_text(text):
    list_of_chars = list(text)
    output_chars = []

    for let in list_of_chars:
        new_char = __rotate_character(let)
        output_chars.append(new_char)

    return ''.join(output_chars)


def decrypt(encrypted_text, mov):
    global move_length
    increment = int(mov / let_length) + 1
    move_length = (let_length * increment) - mov
    return __transform_text(encrypted_text)


def encrypt(text_to_encrypt, mov):
    global move_length
    move_length = mov
    return __transform_text(text_to_encrypt)


def bruteforce_decrypt(text_to_decrypt):
    output_array = []
    for i, nbr in enumerate(letters):
        ind = i + 1
        output_array.append(decrypt(text_to_decrypt, ind))

    return output_array
