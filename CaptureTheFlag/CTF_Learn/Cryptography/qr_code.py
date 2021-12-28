# Exercise: https://ctflearn.com/challenge/228
# ROT_13: https://practical.li/clojure/images/caesar-cipher-rot13.png

import sys
sys.path.append('../../../modules/crypto/')
import rot_13_crypto

base64_text = 'c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI='


encrypted_text = 'synt vf : a0_obql_s0etrg_de_pbqr'

decrypted_text = rot_13_crypto.decrypt(encrypted_text)
test = rot_13_crypto.encrypt(decrypted_text)

print(decrypted_text)