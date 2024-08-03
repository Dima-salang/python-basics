"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

"""

"""
Rationale:
    We make a dictionary of the alphabet, numbering 1-26 for A-Z. Since the input is string, we loop over the string.
    The problem is reminiscent of a numbering system, specifically it is a 26-number system. 
    So we just need to calculate each letter's value based on its position in the string.
"""

def titleToNumber(columnTitle):
    alphabet = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
    }

    sum = 0
    position = len(columnTitle)-1
    for letter in columnTitle:
        sum += (26**position) * alphabet[letter]
        position -= 1

    return sum


print(titleToNumber("ZZZA"))



def titleToNumberASCII(colTitle):

    position = len(colTitle)-1
    sum = 0
    for letter in colTitle:
        # get the ascii of the letter and shift it to the original alphabet numbering
        letter = ord(letter) - 64

        # sum all of the letters' values depending on the position based on the numbering system
        sum += (26**position) * letter
        position -= 1
    
    return sum


print(titleToNumber("ZZZA"))





