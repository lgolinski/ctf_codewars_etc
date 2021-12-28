# https://docs.python.org/3/library/functions.html

# -- ================================================== --
#           one line conditional if statement
# -- ================================================== --
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# -- ================================================== --
#                   Lambda in python
# -- ================================================== --
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# -- ================================================== --
#               Slice of array in python
# -- ================================================== --
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

# -- ================================================== --
#           Invert keys with values in dictionary
# -- ================================================== --

morse = {
     'A': '.-'
    ,'B': '-...'
}

morse_inverted = {v: k for k, v in morse.items()}