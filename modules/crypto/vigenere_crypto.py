# TODO: I think that encrypt is not working correctly. Need to look at this.

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
iteration = 0
key = ''
key_length = 0


def __transform_char(let):
    global iteration

    try:
        let_index = letters.index(let.upper())
    except ValueError:
        return let

    if iteration == key_length:
        iteration = 0

    key_code = letters.index(key[iteration])
    decoded_letter = letters[let_index - key_code]
    iteration += 1

    return decoded_letter.upper() if let.isupper() is True else decoded_letter.lower()


def __transform_text(text_to_transform, d_key):
    global key
    key = d_key.upper()
    global key_length
    key_length = len(d_key)

    transformed_array = []
    for enc_letter in text_to_transform:
        transformed_array.append(__transform_char(enc_letter))

    return ''.join(transformed_array)


def decrypt(text_to_decrypt, d_key):
    return __transform_text(text_to_decrypt, d_key)


def encrypt(text_to_decrypt, d_key):
    return __transform_text(text_to_decrypt, d_key)
