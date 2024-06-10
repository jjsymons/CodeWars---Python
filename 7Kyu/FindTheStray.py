"""
https://www.codewars.com/kata/57f609022f4d534f05000024/python

You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""


def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i


print(stray([1, 2, 1, 1, 1, 1, 1]))

"""
import codewars_test as test
from solution import stray

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(stray([1, 1, 1, 1, 1, 1, 2]), 2)
        test.assert_equals(stray([2, 3, 2, 2, 2]), 3)"""
