"""

https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python


Very simple, given an integer or a floating-point number, find its opposite.

Examples:

1: -1
14: -14
-34: 34

"""

def opposite(number):
    return number - (number*2)

print(opposite(6))

