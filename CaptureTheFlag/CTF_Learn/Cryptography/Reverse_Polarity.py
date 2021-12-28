# Full url to this task: https://ctflearn.com/challenge/230
import re

input_data = '01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101'
output_array = re.findall("[0-1]{8}", input_data)

for el in output_array:
    print(chr(int(el, 2)), end="")
