"""This Kata is intended as a small challenge for my students

All Star Code Challenge #18

Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0"""

def str_count(word, letter):
    count = 0
    out = [word] 
    for i in word:
        if word[i] == letter:
            count+=1
        else:
            continue
    return count

print(str_count("Hello", "l"))


"""@test.describe('Should return the correct character count')
def fixed():
    @test.it("")
    def f():
        test.assert_equals(str_count('hello', 'l'), 2)
        test.assert_equals(str_count('hello', 'e'), 1)
        test.assert_equals(str_count('codewars', 'c'), 1)
        test.assert_equals(str_count('ggggg', 'g'), 5)
        test.assert_equals(str_count('hello world', 'o'), 2)
        test.assert_equals(str_count('', 'z'), 0)"""