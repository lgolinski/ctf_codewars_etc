import os
# CTF - https://ctflearn.com/challenge/174
# needed file simple_programming.dat

location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(location, 'simple_programming.dat')) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

total = 0
for line in lines:
    count_0 = line.count('0')
    count_1 = line.count('1')

    if count_0 % 3 == 0 or count_1 % 2 == 0:
        total = total + 1

print(total)

# with open(os.path.join(location, 'decoded.txt'), 'w+') as f:
#     for line in lines:
#         number = int(line,2)
#         f.write('.' + str(number) + '\n')

# Number of lines 10000
# 0 number lines: 537, 6296        