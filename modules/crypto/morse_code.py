morse = {
     'A': '.-'
    ,'B': '-...'
    ,'C': '-.-.'
    ,'D': '-..'
    ,'E': '.'
    ,'F': '..-.'
    ,'G': '--.'
    ,'H': '....'
    ,'I': '..'
    ,'J': '.---'
    ,'K': '-.-'
    ,'L': '.-..'
    ,'M': '--'
    ,'N': '-.'
    ,'O': '---'
    ,'P': '.--.'
    ,'Q': '--.-'
    ,'R': '.-.'
    ,'S': '...'
    ,'T': '-'
    ,'U': '..-'
    ,'V': '...-'
    ,'W': '.--'
    ,'X': '-..-'
    ,'Y': '-.--'
    ,'Z': '--..'
    ,'Ą': '.-.-'
    ,'Ć': '-.-..'
    ,'Ę': '..-..'
    ,'É': '..-..'
    ,'CH': '----'
    ,'Ł': '.-..-'
    ,'Ń': '--.--'
    ,'Ó': '---.'
    ,'Ś': '...-...'
    ,'Ż': '--..-.'
    ,'Ź': '--.-'
    ,'1': '.----'
    ,'2': '..---'
    ,'3': '...--'
    ,'4': '....-'
    ,'5': '.....'
    ,'6': '-....'
    ,'7': '--...'
    ,'8': '---..'
    ,'9': '----.'
    ,'0': '-----'
    ,'.': '.-.-.-'
    ,',': '--..--'
    ,"'": '.----.'
    ,'"': '.-..-.'
    ,'_': '..--.-'
    ,':': '___...'
    ,';': '-.-.-.'
    ,'?': '..--..'
    ,'!': '-.-.--'
    ,'-': '-....-'
    ,'+': '.-.-.'
    ,'/': '-..-.'
    ,'(': '-.--.'
    ,')': '-.--.-'
    ,'=': '_..._'
    ,'@': '.--.-.'
}


def __find_letter_from_morse(morse_letter):
    for key, value in morse.items():
        if value == morse_letter:
            return key
    return ''


def decrypt(text_to_decrypt):
    output_array = []
    code_array = text_to_decrypt.split(' ')

    for letter in code_array:
        output_array.append(__find_letter_from_morse(letter))

    return ''.join(output_array)


def encrypt(text_to_encrypt):
    output_array = []
    list_of_chars = list(text_to_encrypt)

    for letter in list_of_chars:
        output_array.append(morse[letter])
        output_array.append(' ')

    return ''.join(output_array)
