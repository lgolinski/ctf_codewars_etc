# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
# https://en.wikipedia.org/wiki/Digital_root
# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this
# way until a single-digit number is produced. The input will be a non-negative integer.

# EXAMPLES
#
# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    # convert int value to string and iterate on them
    strNum = str(n)
    sum = 0
    for str_digit in strNum:
        sum = sum + int(str_digit)
    
    if(sum > 9):
        sum = digital_root(sum)

    return sum

# Sample usage
print(digital_root(493193))