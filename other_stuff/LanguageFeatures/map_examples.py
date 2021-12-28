# https://docs.python.org/3/library/functions.html#map
# -- ================================================== --
#               Python map() examples
#      Its syntax is: map(function, iterable, ...)
# -- ================================================== --

# Example 1: Working of map()

# ================================================
numbers = [2, 4, 6, 8, 10]
# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# Output: [4, 16, 36, 64, 100]   

# ================================================

def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

# Output: <map object at 0x7f722da129e8>
#         {16, 1, 4, 9}

# ================================================



# Example 2: How to use lambda function with map()?

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)