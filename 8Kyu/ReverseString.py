"""

https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

"""
def solution(string):
    reversedString = string[::-1]
    return reversedString

print(solution("Hello"))