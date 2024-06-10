"""

https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python


This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

"""

def accum(s):
    output = ""
    i = 0
    while i < len(s):
        if i == 0:
            output += s[i].upper()
        else:
            output += "-" + s[i].upper()
            output += s[i].lower()*i
        i+=1
    return output


print(accum("ZpglnRxqenU"))

#outputs "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"