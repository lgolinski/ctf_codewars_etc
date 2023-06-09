# Full url to this task: https://ctflearn.com/challenge/158
# Youtube Videos The Bacon Cipher Explained: 
#   *   https://www.youtube.com/watch?v=SXOoICf2DgU
#   *   https://www.youtube.com/watch?v=ctA38iXUpYg

#   I love the smell of bacon in the morning! 
#   ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB 

import sys
sys.path.append('../../../modules/crypto/')
import bacons_crypto


text_to_decrypt = 'ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB'

decrypted_text = bacons_crypto.decrypt(text_to_decrypt)
print(decrypted_text)

encrypted_text = bacons_crypto.encrypt('Youtube Videos The Bacon Cipher Explained', True)
print(encrypted_text)