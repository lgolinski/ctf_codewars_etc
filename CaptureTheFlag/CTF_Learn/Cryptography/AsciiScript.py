encoded_text = '67 84 70 108 101 97 110 123 67 82 89 80 84 79 71 82 65 80 72 89 125'

#[expression for item in list]
arr_text = [chr(int(i)) for i in encoded_text.split()]

print(''.join(arr_text))