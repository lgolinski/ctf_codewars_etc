# TODO: After 100 movements encryption, decryption have problem. Need to fix this.

min_ascii_value = 32
max_ascii_value = 126
let_length = (max_ascii_value - min_ascii_value) + 1


def __transform_character(ascii_char, mov):
    ascii_letter = ord(ascii_char) + mov

    if ascii_letter > max_ascii_value:
        left_val = (ascii_letter - max_ascii_value - 1) + min_ascii_value
        return chr(left_val)

    return chr(ascii_letter)


def __transform_text(text_to_decrypt, mov):
    list_of_chars = list(text_to_decrypt)
    transformed_array = []
    for key in list_of_chars:
        transformed_char = __transform_character(key, mov)
        transformed_array.append(transformed_char)

    return ''.join(transformed_array)


def decrypt(text_to_decrypt, mov):
    increment = int(mov / let_length) + 1
    move_length = (let_length * increment) - mov

    return __transform_text(text_to_decrypt, move_length)


def encrypt(text_to_encrypt, mov):
    return __transform_text(text_to_encrypt, mov)


def bruteforce_decrypt(text_to_decrypt):
    output_array = []
    for i, nbr in enumerate(range(min_ascii_value, max_ascii_value)):
        ind = i + 1
        output_array.append(decrypt(text_to_decrypt, ind))

    return output_array
