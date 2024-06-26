"""

https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python


You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
"""

def find_next_square(sq):
    iterator = 1
    while iterator*iterator < sq +1:
        iterator +=1
    if sq % iterator -1 == 0:
        return iterator * iterator
    else:
        return -1

print(find_next_square(120))