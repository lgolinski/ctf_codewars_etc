# Bacon's Cipher Explained: 
#   *   https://en.wikipedia.org/wiki/Bacon%27s_cipher

# Youtube Videos The Bacon Cipher Explained: 
#   *   https://www.youtube.com/watch?v=SXOoICf2DgU
#   *   https://www.youtube.com/watch?v=ctA38iXUpYg

v1_table = {
    'A' : { 'Code' : 'aaaaa', 'Binary' : b'00000' },
    'B' : { 'Code' : 'aaaab', 'Binary' : b'00001' },
    'C' : { 'Code' : 'aaaba', 'Binary' : b'00010' },
    'D' : { 'Code' : 'aaabb', 'Binary' : b'00011' },
    'E' : { 'Code' : 'aabaa', 'Binary' : b'00100' },
    'F' : { 'Code' : 'aabab', 'Binary' : b'00101' },
    'G' : { 'Code' : 'aabba', 'Binary' : b'00110' },
    'H' : { 'Code' : 'aabbb', 'Binary' : b'00111' },
    'I' : { 'Code' : 'abaaa', 'Binary' : b'01000' },

    # J does Not exists in this version of script and shoud be replaced with I    
    'J' : { 'Code' : 'abaaa', 'Binary' : b'01000' },
    'K' : { 'Code' : 'abaab', 'Binary' : b'01001' },
    'L' : { 'Code' : 'ababa', 'Binary' : b'01010' },
    'M' : { 'Code' : 'ababb', 'Binary' : b'01011' },
    'N' : { 'Code' : 'abbaa', 'Binary' : b'01100' },
    'O' : { 'Code' : 'abbab', 'Binary' : b'01101' },
    'P' : { 'Code' : 'abbba', 'Binary' : b'01110' },
    'Q' : { 'Code' : 'abbbb', 'Binary' : b'01111' },
    'R' : { 'Code' : 'baaaa', 'Binary' : b'10000' },
    'S' : { 'Code' : 'baaab', 'Binary' : b'10001' },
    'T' : { 'Code' : 'baaba', 'Binary' : b'10010' },
    'U' : { 'Code' : 'baabb', 'Binary' : b'10011' },

    # V does Not exists in this version of script and shoud be replaced with U
    'V' : { 'Code' : 'baabb', 'Binary' : b'10011' },
    'W' : { 'Code' : 'babaa', 'Binary' : b'10100' },
    'X' : { 'Code' : 'babab', 'Binary' : b'10101' },
    'Y' : { 'Code' : 'babba', 'Binary' : b'10110' },
    'Z' : { 'Code' : 'babbb', 'Binary' : b'10111' }, 
}

v2_table = {
    'A' : { 'Code' : 'aaaaa', 'Binary' : b'00000' },
    'B' : { 'Code' : 'aaaab', 'Binary' : b'00001' },
    'C' : { 'Code' : 'aaaba', 'Binary' : b'00010' },
    'D' : { 'Code' : 'aaabb', 'Binary' : b'00011' },
    'E' : { 'Code' : 'aabaa', 'Binary' : b'00100' },
    'F' : { 'Code' : 'aabab', 'Binary' : b'00101' },
    'G' : { 'Code' : 'aabba', 'Binary' : b'00110' },
    'H' : { 'Code' : 'aabbb', 'Binary' : b'00111' },
    'I' : { 'Code' : 'abaaa', 'Binary' : b'01000' },
    'J' : { 'Code' : 'abaab', 'Binary' : b'01001' },
    'K' : { 'Code' : 'ababa', 'Binary' : b'01010' },
    'L' : { 'Code' : 'ababb', 'Binary' : b'01011' },
    'M' : { 'Code' : 'abbaa', 'Binary' : b'01100' },
    'N' : { 'Code' : 'abbab', 'Binary' : b'01101' },
    'O' : { 'Code' : 'abbba', 'Binary' : b'01110' },
    'P' : { 'Code' : 'abbbb', 'Binary' : b'01111' },
    'Q' : { 'Code' : 'baaaa', 'Binary' : b'10000' },
    'R' : { 'Code' : 'baaab', 'Binary' : b'10001' },
    'S' : { 'Code' : 'baaba', 'Binary' : b'10010' },
    'T' : { 'Code' : 'baabb', 'Binary' : b'10011' },
    'U' : { 'Code' : 'babaa', 'Binary' : b'10100' },
    'V' : { 'Code' : 'babab', 'Binary' : b'10101' },
    'W' : { 'Code' : 'babba', 'Binary' : b'10110' },
    'X' : { 'Code' : 'babbb', 'Binary' : b'10111' },
    'Y' : { 'Code' : 'bbaaa', 'Binary' : b'11000' },
    'Z' : { 'Code' : 'bbaab', 'Binary' : b'11001' }, 
}
    

def decrypt(encrypted_text: str, fullVersion: bool = False) -> str:
    encrypted_text = encrypted_text.replace(' ', '')
    endIndex = 5
    result = ''

    for startIndex in range(0, len(encrypted_text), 5):
        code = encrypted_text[startIndex:endIndex]
        letter = __find_letter_from_code(code, fullVersion)
        result = result + letter
        endIndex = endIndex + 5

    return result


def encrypt(text_to_encrypt: str, fullVersion: bool = False) -> str:
    result_encrypted = ''

    for letter in text_to_encrypt:
        if not __is_valid_letter(letter):
            continue

        code = __find_code_for_letter(letter, fullVersion)
        result_encrypted = result_encrypted + code + ' '

    return result_encrypted


def __find_code_for_letter(letter: str, fullVersion: bool) -> str:
    findInTable = v1_table

    if fullVersion == True:
        findInTable = v2_table 

    value = findInTable[letter.upper()]
    return value['Code']


def __is_valid_letter(letter: chr) -> bool:
    lett_in_ascii = ord(letter)

    if lett_in_ascii >= ord('A') and lett_in_ascii <= ord('Z'):
        return True 

    if lett_in_ascii >= ord('a') and lett_in_ascii <= ord('z'):
        return True 
    
    return False


def __find_letter_from_code(searchCode: str, fullVersion: bool) -> chr:
    searchCode = searchCode.lower()
    return_key = ''
    findInTable = v1_table

    if fullVersion == True:
        findInTable = v2_table 

    for key in findInTable.keys():
        if searchCode == findInTable[key]['Code']:
            return_key = key
            break
    
    return return_key

