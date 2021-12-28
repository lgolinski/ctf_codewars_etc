# Full url to this task: https://ctflearn.com/challenge/305
# Usefull videos: * https://www.youtube.com/watch?v=SkJcmCaHqS0
#                 * https://www.youtube.com/watch?v=oHcJ4QLiiP8

import sys
sys.path.append('../../../modules/crypto/')
import vigenere_crypto

encrypted_message = 'gwox{RgqssihYspOntqpxs}'
key = 'blorpy'

decrypted_text = vigenere_crypto.decrypt(encrypted_message, key)
print(decrypted_text)
