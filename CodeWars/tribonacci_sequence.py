# Tribonacci Sequence
# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def tribonacci(signature, n):
    if n == 0:
        return []

    input_size = len(signature)
    # return only slice of array
    if n < input_size:
        return signature[:n]

    output_array = signature + ([None] * (n - input_size))
    
    for ind, val in enumerate(output_array):
        if val is not None:
            continue

        output_array[ind] = sum(output_array[ind-3 : ind])

    return output_array

print(tribonacci([1, 1, 1], 1))