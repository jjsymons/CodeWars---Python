"""

https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python

Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

"""


def boolean_to_string(b):
    if b:
        return 'True'
    return 'False'


"""
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(boolean_to_string(True), "True")
        test.assert_equals(boolean_to_string(False), "False")
"""
