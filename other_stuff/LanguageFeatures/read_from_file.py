import os

location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(location, 'i_am_a_dump.dat'), 'rb') as f:
    hexdata = f.read().hex()

bytearray.fromhex("7061756c").decode()
