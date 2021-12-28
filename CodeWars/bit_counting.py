# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
# You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def isNotNegativeNumber(n):
    if(type(n) is not int):
        return False

    if(n < 0):
        return False

    return True

def count_bits(n):
    if(not isNotNegativeNumber(n)):
        return 0

    # -2 because string representation of bits starts with 0b...... so we delete this 2 chars from len.
    number_of_bits = len(bin(n)) - 2
    bitsFormatOfNumber = [(n >> bit) & 1 for bit in range(number_of_bits -1,-1,-1)]
    
    return bitsFormatOfNumber.count(1)

# Sample usage
print(count_bits(1234))
