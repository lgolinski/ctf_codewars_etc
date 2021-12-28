# Full url to this task: https://ctflearn.com/challenge/309
# Morse Code informations: https://pl.wikipedia.org/wiki/Kod_Morse%E2%80%99a
import sys
sys.path.append('../../../modules/crypto/')
import morse_code

text_to_decrypt = '..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...'

decrypted_text = morse_code.decrypt(text_to_decrypt)

print('------------------- MORSE CODE DECRYPTED -------------------')
print('')
print(decrypted_text)
print('')
print('------------------------------------------------------------')
