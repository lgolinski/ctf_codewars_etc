# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!

def get_sum(a,b):
    if(a == b):
        return a

    return sum(range(min(a,b), max(a,b) + 1))

print(get_sum(0,-1))    