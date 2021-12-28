# Full url to this task: https://ctflearn.com/challenge/115

encoded_data = '41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D'
encoded_array = encoded_data.split(' ')
output_text = ''

for el in encoded_array:
    output_text = output_text + chr(int(el, 16))

print(output_text)
