'''Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, 
starting with the leftmost digit and skipping any 0s. 
So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). 
The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:'''

# solution('XXI') # should return 21


'''Help:'''

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

'''Courtesy of rosettacode.org'''

# ----start of solution----

# Time: 560ms Passed: 98, Failed: 9, Exit Code: 1
# Work in progress

roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
def solution(input):
    output = 0
    start = 0
    
    if len(input) > 1:
            if input[0:2] == 'CD':
                output += 400
                start = 2
    for i in range(start, len(input)):
        if input[i] != 'I':
            if input[i] == 'X':
                if (i < (len(input) - 1) and (input[i + 1] == 'L' or input[i + 1] == 'C')):
                    output -= 10
                else:
                    output += roman_dict[input[i]]
            elif input[i] == 'C':
                if (i < (len(input) - 1) and (input[i + 1] == 'M')):
                    output -= 100
                else:
                    output += roman_dict[input[i]]
            else:
                output += roman_dict[input[i]]
        else:              
            if input[-1] in 'XV':
                output -= 1
            else:
                output += roman_dict[input[i]]

    return output