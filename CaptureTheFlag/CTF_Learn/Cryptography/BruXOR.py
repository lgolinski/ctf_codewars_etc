import itertools
# Full url to this task: https://ctflearn.com/challenge/227
# More informations about BruteForce can be found here: https://pl.wikipedia.org/wiki/Atak_brute_force
# Since this should be an easy task I'll try to use ASCII code convert first. 
# Somethings similar to decode cesar cripting.

encoded_message = "q{vpln'bH_varHuebcrqxetrHOXEj"
list_of_chars = list(encoded_message)
ascii_chars = []
bit_version_of_text = []
transformed_code = ''

# Try to gues that this are only ascii english characters. 
# So for the range i will get numbers from 32 to 126
min_ascii_value = 32
max_ascii_value = 126

def transformCharacter(ascii_letter):
    if(ascii_letter == max_ascii_value):
        return min_ascii_value
    
    return ascii_letter + 1


for char in list_of_chars:
    ascii_chars.append(ord(char))

for el in ascii_chars:
    bit_version_of_text.append(bin(el))
    print(bin(el))

all_posible_combinations = [list(i) for i in itertools.product([0, 1], repeat=7)]

while(transformed_code != encoded_message):
    transformed_code = ''
    transormed_array = []
    for key in ascii_chars:
        transformed_char = transformCharacter(key)
        transormed_array.append(transformed_char)
        transformed_code = transformed_code + chr(transformed_char)

    ascii_chars = transormed_array.copy()
    print(transformed_code)

# print("")
# print("Sure, It can't be that easy. Lets try something with task name. There is XOR operator in name.")
# print("It can be combination of movement")

# Now I know that here is use XOR Cripting, let's try to do something with this knowledge.




