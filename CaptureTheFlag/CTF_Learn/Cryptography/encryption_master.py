# help 1: https://www.rapidtables.com/code/text/ascii-table.html
# help 2: https://stackoverflow.com/questions/9641440/convert-from-ascii-string-encoded-in-hex-to-plain-ascii
# help 3: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa

import base64

# This is NOT going to be fun.
first_encoding = b'TmljZSEgTm93IGtlZXAgZ29pbmcuIDU0Nzc2ZjIwNmQ2ZjcyNjUyZTIwMzAzMTMwMzAzMDMxMzEzMDIwMzAzMTMxMzAzMTMwMzAzMTIwMzAzMTMxMzAzMTMxMzEzMDIwMzAzMTMxMzAzMDMwMzAzMTIwMzAzMTMxMzAzMTMxMzAzMDIwMzAzMDMxMzAzMDMwMzAzMDIwMzAzMTMwMzAzMDMxMzAzMDIwMzAzMTMxMzAzMDMxMzAzMTIwMzAzMTMxMzAzMDMwMzEzMTIwMzAzMTMxMzEzMDMwMzEzMDIwMzAzMTMxMzEzMTMwMzAzMTIwMzAzMTMxMzEzMDMwMzAzMDIwMzAzMTMxMzEzMDMxMzAzMDIwMzAzMTMxMzAzMTMwMzAzMTIwMzAzMTMxMzAzMTMxMzEzMTIwMzAzMTMxMzAzMTMxMzEzMDIwMzAzMDMxMzAzMDMwMzAzMTIwMzAzMDMxMzAzMDMwMzAzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMDMxMzEzMDMwMzAzMTIwMzAzMTMwMzEzMDMwMzEzMDIwMzAzMTMwMzAzMDMxMzEzMTIwMzAzMTMxMzAzMDMxMzAzMTIwMzAzMDMxMzEzMDMwMzAzMDIwMzAzMTMxMzAzMTMxMzAzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMDMxMzEzMDMwMzAzMTIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMTMwMzAzMDMxMzEzMDIwMzAzMTMwMzAzMTMwMzEzMDIwMzAzMTMwMzEzMDMwMzAzMDIwMzAzMTMwMzEzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMTMwMzEzMDMwMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMDIwMzAzMDMxMzEzMDMwMzAzMDIwMzAzMTMwMzEzMTMwMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzEzMTIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMDMxMzEzMTMwMzAzMTIwMzAzMTMwMzEzMDMxMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMDMxMzEzMTMxMzAzMTIwMzAzMDMxMzEzMTMxMzAzMQ=='

# Nice! Now keep going.
second_encoding = '54776f206d6f72652e203031303030313130203031313031303031203031313031313130203031313030303031203031313031313030203030313030303030203031303030313030203031313030313031203031313030303131203031313130303130203031313131303031203031313130303030203031313130313030203031313031303031203031313031313131203031313031313130203030313030303031203030313030303030203031303130303031203030313130303031203031303130303130203031303030313131203031313030313031203030313130303030203031313031313030203031313030313130203031303130303031203031303130313031203030313130303031203031313030313130203031303130313031203031303030313130203031303031303130203031303130303030203031303130313130203031303130313031203031303130303130203031313030313130203031303130313030203030313130303030203031303131303130203031313030313130203031303130313131203031303130313031203030313131303031203031303130313130203031313030313130203031303130303031203030313131313031203030313131313031'

#Two more. 
third_encoding = '0100011001101001011011100110000101101100001000000100010001100101011000110111001001111001011100000111010001101001011011110110111000100001001000000101000100110001010100100100011101100101001100000110110001100110010100010101010100110001011001100101010101000110010010100101000001010110010101010101001001100110010101000011000001011010011001100101011101010101001110010101011001100110010100010011110100111101'

# Final Decryption!
final_encoding = 'Q1RGe0lfQU1fUFJPVURfT0ZfWU9VfQ=='

print('-- ================================================================= --')
print('--                          ENCODED TEXT                             --')
print('-- ================================================================= --')
print()

print('This is NOT going to be fun. TmljZSEgTm93IGtlZXAgZ29pbmcuIDU0Nzc2ZjIwNmQ2ZjcyNjUyZTIwMzAzMTMwMzAzMDMxMzEzMDIwMzAzMTMxMzAzMTMwMzAzMTIwMzAzMTMxMzAzMTMxMzEzMDIwMzAzMTMxMzAzMDMwMzAzMTIwMzAzMTMxMzAzMTMxMzAzMDIwMzAzMDMxMzAzMDMwMzAzMDIwMzAzMTMwMzAzMDMxMzAzMDIwMzAzMTMxMzAzMDMxMzAzMTIwMzAzMTMxMzAzMDMwMzEzMTIwMzAzMTMxMzEzMDMwMzEzMDIwMzAzMTMxMzEzMTMwMzAzMTIwMzAzMTMxMzEzMDMwMzAzMDIwMzAzMTMxMzEzMDMxMzAzMDIwMzAzMTMxMzAzMTMwMzAzMTIwMzAzMTMxMzAzMTMxMzEzMTIwMzAzMTMxMzAzMTMxMzEzMDIwMzAzMDMxMzAzMDMwMzAzMTIwMzAzMDMxMzAzMDMwMzAzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMDMxMzEzMDMwMzAzMTIwMzAzMTMwMzEzMDMwMzEzMDIwMzAzMTMwMzAzMDMxMzEzMTIwMzAzMTMxMzAzMDMxMzAzMTIwMzAzMDMxMzEzMDMwMzAzMDIwMzAzMTMxMzAzMTMxMzAzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMDMxMzEzMDMwMzAzMTIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMTMwMzAzMDMxMzEzMDIwMzAzMTMwMzAzMTMwMzEzMDIwMzAzMTMwMzEzMDMwMzAzMDIwMzAzMTMwMzEzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMTMwMzEzMDMwMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzAzMDIwMzAzMDMxMzEzMDMwMzAzMDIwMzAzMTMwMzEzMTMwMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMxMzEzMTIwMzAzMTMwMzEzMDMxMzAzMTIwMzAzMDMxMzEzMTMwMzAzMTIwMzAzMTMwMzEzMDMxMzEzMDIwMzAzMTMxMzAzMDMxMzEzMDIwMzAzMTMwMzEzMDMwMzAzMTIwMzAzMDMxMzEzMTMxMzAzMTIwMzAzMDMxMzEzMTMxMzAzMQ==')
print()
print('-- ================================================================= --')
print()

print('-- ================================================================= --')
print('--                      FIRST DECRYPTION                             --')
print('-- ================================================================= --')
print()

first_decode = base64.b64decode(first_encoding)

print(first_decode)
print()
print('-- ================================================================= --')
print()


print('-- ================================================================= --')
print('--                      SECOND DECRYPTION                            --')
print('-- ================================================================= --')
print()

second_decode = bytearray.fromhex(second_encoding).decode()

print(second_decode)

print()
print('-- ================================================================= --')
print()

print('-- ================================================================= --')
print('--                       THIRD DECRYPTION                            --')
print('-- ================================================================= --')
print()

n = int('0b' + third_encoding, 2)
third_decoded = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
print(third_decoded)

print()
print('-- ================================================================= --')
print()

print('-- ================================================================= --')
print('--                        FINAL DECRYPTION                           --')
print('-- ================================================================= --')
print()

final_decrypt = base64.b64decode(final_encoding)
print(final_decrypt)

print()
print('-- ================================================================= --')
print()